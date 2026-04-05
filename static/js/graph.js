/**
 * QuantiesUnite — Interactive Curriculum Graph
 * D3.js v7 force-directed graph with:
 *   - Hover: highlight ALL connected nodes + edges (ancestors & descendants)
 *   - Click: navigate to topic page
 *   - Zoom & pan
 *   - Search filter
 *   - Level filter
 */

(async function () {
  const W = window.innerWidth;
  const H = window.innerHeight - 56; // subtract toolbar height

  // ── Fetch Data ──────────────────────────────────────────────────────────────
  const data = await d3.json("/api/graph");
  let allNodes = data.nodes;
  let allLinks = data.links;

  // ── State ───────────────────────────────────────────────────────────────────
  let selectedNode = null;
  let clickTimer = null;
  let _tooltipDragging = false;

  // ── SVG & zoom setup ────────────────────────────────────────────────────────
  const svg = d3.select("#graph-svg")
    .attr("width", W)
    .attr("height", H);

  const g = svg.append("g").attr("class", "graph-root");

  const zoom = d3.zoom()
    .scaleExtent([0.15, 3])
    .on("zoom", (event) => g.attr("transform", event.transform));

  svg.call(zoom);

  // ── Arrow marker ────────────────────────────────────────────────────────────
  svg.append("defs").append("marker")
    .attr("id", "arrowhead")
    .attr("viewBox", "0 -5 10 10")
    .attr("refX", 22)
    .attr("refY", 0)
    .attr("markerWidth", 6)
    .attr("markerHeight", 6)
    .attr("orient", "auto")
    .append("path")
    .attr("d", "M0,-5L10,0L0,5")
    .attr("fill", "#555");

  // Prereq arrows (green — leads TO the hovered node)
  svg.append("defs").append("marker")
    .attr("id", "arrowhead-prereq")
    .attr("viewBox", "0 -5 10 10")
    .attr("refX", 22).attr("refY", 0)
    .attr("markerWidth", 6).attr("markerHeight", 6)
    .attr("orient", "auto")
    .append("path")
    .attr("d", "M0,-5L10,0L0,5")
    .attr("fill", "#22c55e");

  // Downstream arrows (yellow — leads AWAY from the hovered node)
  svg.append("defs").append("marker")
    .attr("id", "arrowhead-downstream")
    .attr("viewBox", "0 -5 10 10")
    .attr("refX", 22).attr("refY", 0)
    .attr("markerWidth", 6).attr("markerHeight", 6)
    .attr("orient", "auto")
    .append("path")
    .attr("d", "M0,-5L10,0L0,5")
    .attr("fill", "#FFD700");

  // ── Force simulation ────────────────────────────────────────────────────────
  let simulation = d3.forceSimulation(allNodes)
    .force("link", d3.forceLink(allLinks)
      .id(d => d.id)
      .distance(110)
      .strength(0.6))
    .force("charge", d3.forceManyBody().strength(-400))
    .force("center", d3.forceCenter(W / 2, H / 2))
    .force("collide", d3.forceCollide(38))
    .force("x", d3.forceX(W / 2).strength(0.04))
    .force("y", d3.forceY(H / 2).strength(0.04));

  // ── Draw links ──────────────────────────────────────────────────────────────
  let linkSel = g.append("g").attr("class", "links")
    .selectAll("line")
    .data(allLinks)
    .join("line")
    .attr("class", "graph-link")
    .attr("stroke", "#444")
    .attr("stroke-width", 1.5)
    .attr("stroke-opacity", 0.5)
    .attr("marker-end", "url(#arrowhead)");

  // ── Draw nodes ──────────────────────────────────────────────────────────────
  let nodeSel = g.append("g").attr("class", "nodes")
    .selectAll("g")
    .data(allNodes)
    .join("g")
    .attr("class", "graph-node")
    .call(drag(simulation))
    .on("click", (event, d) => {
      event.stopPropagation();
      // Single click = select node and show card
      if (clickTimer) { clearTimeout(clickTimer); clickTimer = null; }
      clickTimer = setTimeout(() => {
        clickTimer = null;
        selectNode(d, event);
      }, 250);
    })
    .on("dblclick", (event, d) => {
      event.stopPropagation();
      if (clickTimer) { clearTimeout(clickTimer); clickTimer = null; }
      window.location.href = "/topic/" + d.id + "/overview";
    })
    .on("mouseenter", (event, d) => { if (!selectedNode) handleHover(d, true); })
    .on("mouseleave", (event, d) => { if (!selectedNode) handleHover(d, false); });

  // Node circles
  nodeSel.append("circle")
    .attr("r", d => d.complete ? 20 : 16)
    .attr("fill", d => d.color)
    .attr("stroke", d => d.complete ? "#fff" : (d.unlocked ? d.color : "#666"))
    .attr("stroke-width", d => d.complete ? 3 : 2)
    .attr("fill-opacity", d => d.unlocked ? 1.0 : 0.35)
    .attr("class", "node-circle");

  // Emoji label
  nodeSel.append("text")
    .attr("text-anchor", "middle")
    .attr("dy", "0.35em")
    .attr("font-size", "13px")
    .attr("pointer-events", "none")
    .text(d => d.emoji);

  // Name label (below circle)
  nodeSel.append("text")
    .attr("text-anchor", "middle")
    .attr("dy", "30px")
    .attr("font-size", "9px")
    .attr("fill", "#ccc")
    .attr("pointer-events", "none")
    .attr("class", "node-label")
    .text(d => truncate(d.name, 18));

  // Completion ring
  nodeSel.filter(d => d.complete)
    .append("circle")
    .attr("r", 8)
    .attr("cx", 12)
    .attr("cy", -12)
    .attr("fill", "#22c55e")
    .attr("stroke", "#111")
    .attr("stroke-width", 1);

  nodeSel.filter(d => d.complete)
    .append("text")
    .attr("x", 12).attr("y", -8)
    .attr("text-anchor", "middle")
    .attr("font-size", "8px")
    .text("✓");

  // ── Tick ────────────────────────────────────────────────────────────────────
  simulation.on("tick", () => {
    linkSel
      .attr("x1", d => d.source.x)
      .attr("y1", d => d.source.y)
      .attr("x2", d => d.target.x)
      .attr("y2", d => d.target.y);
    nodeSel.attr("transform", d => `translate(${d.x},${d.y})`);
  });

  // ── Hover: highlight connected graph ────────────────────────────────────────
  function getConnected(node) {
    const nodeSet = new Set([node.id]);
    const upstreamLinks = new Set();
    const downstreamLinks = new Set();

    // Build adjacency
    const upstream = {};
    const downstream = {};
    allLinks.forEach((l, i) => {
      const s = l.source.id || l.source;
      const t = l.target.id || l.target;
      if (!downstream[s]) downstream[s] = [];
      if (!upstream[t]) upstream[t] = [];
      downstream[s].push({ node: t, idx: i });
      upstream[t].push({ node: s, idx: i });
    });

    // BFS upward (prerequisites → green)
    let queue = [node.id];
    while (queue.length) {
      const cur = queue.shift();
      (upstream[cur] || []).forEach(({ node: n, idx }) => {
        upstreamLinks.add(idx);
        if (!nodeSet.has(n)) { nodeSet.add(n); queue.push(n); }
      });
    }
    // BFS downward (what this unlocks → yellow)
    queue = [node.id];
    while (queue.length) {
      const cur = queue.shift();
      (downstream[cur] || []).forEach(({ node: n, idx }) => {
        downstreamLinks.add(idx);
        if (!nodeSet.has(n)) { nodeSet.add(n); queue.push(n); }
      });
    }
    const linkSet = new Set([...upstreamLinks, ...downstreamLinks]);
    return { nodeSet, linkSet, upstreamLinks, downstreamLinks };
  }

  function handleHover(d, entering) {
    if (entering) {
      const { nodeSet, upstreamLinks, downstreamLinks } = getConnected(d);
      nodeSel.attr("opacity", 0.12);
      linkSel.attr("stroke-opacity", 0.05).attr("stroke", "#444").attr("marker-end", "url(#arrowhead)");
      nodeSel.filter(n => nodeSet.has(n.id)).attr("opacity", 1);
      // Prereq arrows = green
      linkSel.filter((l, i) => upstreamLinks.has(i))
        .attr("stroke", "#22c55e").attr("stroke-opacity", 1)
        .attr("stroke-width", 2.5).attr("marker-end", "url(#arrowhead-prereq)");
      // Downstream arrows = yellow
      linkSel.filter((l, i) => downstreamLinks.has(i))
        .attr("stroke", "#FFD700").attr("stroke-opacity", 1)
        .attr("stroke-width", 2.5).attr("marker-end", "url(#arrowhead-downstream)");
      showTooltipHover(d);
    } else {
      nodeSel.attr("opacity", 1);
      linkSel.attr("stroke", "#444").attr("stroke-opacity", 0.5)
        .attr("stroke-width", 1.5).attr("marker-end", "url(#arrowhead)");
      hideTooltip();
    }
  }

  // ── Tooltip ─────────────────────────────────────────────────────────────────
  const tooltip = document.getElementById("graph-tooltip");

  function fillTooltipContent(d) {
    document.getElementById("tt-emoji").textContent = d.emoji;
    document.getElementById("tt-name").textContent = d.name;
    document.getElementById("tt-level").textContent = d.level + " · " + d.sg;
    document.getElementById("tt-tagline").textContent = d.tagline;
    document.getElementById("tt-hours").textContent = "⏱️ ~" + d.hours + "h study";
    const statusEl = document.getElementById("tt-status");
    if (d.complete) {
      statusEl.textContent = "✅ Complete" + (d.quiz_score !== null && d.quiz_score !== undefined ? " · Quiz: " + d.quiz_score + "/" + d.quiz_total : "");
      statusEl.style.color = "#22c55e";
    } else if (d.unlocked) {
      statusEl.textContent = "🔓 Ready to learn";
      statusEl.style.color = "#FFD700";
    } else {
      statusEl.textContent = "🔒 Complete prerequisites first";
      statusEl.style.color = "#888";
    }
  }

  function showTooltipHover(d) {
    fillTooltipContent(d);
    document.getElementById("tt-actions").style.display = "none";
    tooltip.style.pointerEvents = "none";
    tooltip.classList.remove("hidden");
  }

  svg.on("mousemove", function(event) {
    if (!selectedNode) {
      tooltip.style.left = (event.clientX + 18) + "px";
      tooltip.style.top = (event.clientY - 10) + "px";
    }
  });

  function hideTooltip() {
    tooltip.classList.add("hidden");
    tooltip.style.pointerEvents = "none";
  }

  // ── Select node (single click) — pin tooltip with action buttons ───────────
  function selectNode(d, event) {
    if (selectedNode && selectedNode.id === d.id) {
      deselectNode();
      return;
    }
    selectedNode = d;

    const { nodeSet, upstreamLinks, downstreamLinks } = getConnected(d);
    nodeSel.attr("opacity", 0.12);
    linkSel.attr("stroke-opacity", 0.05).attr("stroke", "#444").attr("marker-end", "url(#arrowhead)");
    nodeSel.filter(n => nodeSet.has(n.id)).attr("opacity", 1);
    // Prereq arrows = green
    linkSel.filter((l, i) => upstreamLinks.has(i))
      .attr("stroke", "#22c55e").attr("stroke-opacity", 1)
      .attr("stroke-width", 2.5).attr("marker-end", "url(#arrowhead-prereq)");
    // Downstream arrows = yellow
    linkSel.filter((l, i) => downstreamLinks.has(i))
      .attr("stroke", "#FFD700").attr("stroke-opacity", 1)
      .attr("stroke-width", 2.5).attr("marker-end", "url(#arrowhead-downstream)");

    // Pin tooltip near the node
    fillTooltipContent(d);
    const transform = d3.zoomTransform(svg.node());
    const screenX = transform.applyX(d.x);
    const screenY = transform.applyY(d.y);
    tooltip.style.left = (screenX + 30) + "px";
    tooltip.style.top = (screenY - 10) + "px";
    tooltip.style.pointerEvents = "auto";
    tooltip.classList.remove("hidden");

    // Show action buttons
    const actionsEl = document.getElementById("tt-actions");
    const targetBtn = document.getElementById("tt-target-btn");
    const enterBtn = document.getElementById("tt-enter-btn");
    actionsEl.style.display = "block";

    enterBtn.onclick = (e) => { e.stopPropagation(); window.location.href = "/topic/" + d.id + "/overview"; };

    if (userTargets.has(d.id)) {
      targetBtn.textContent = "✕ Remove Target";
      targetBtn.onclick = (e) => { e.stopPropagation(); toggleTarget(d.id, false); };
    } else {
      targetBtn.textContent = "🎯 Add Target";
      targetBtn.onclick = (e) => { e.stopPropagation(); toggleTarget(d.id, true); };
    }

    const mindmapBtn = document.getElementById("tt-mindmap-btn");
    if (d.complete || (typeof IS_ADMIN !== 'undefined' && IS_ADMIN)) {
      mindmapBtn.style.display = "block";
      mindmapBtn.onclick = (e) => { e.stopPropagation(); window.location.href = "/topic/" + d.id + "/mindmap"; };
    } else {
      mindmapBtn.style.display = "none";
    }

    // Make tooltip clickable to enter module (but not when dragging)
    tooltip.style.cursor = "pointer";
    tooltip.onclick = (e) => {
      if (e.target.tagName === "BUTTON") return;
      if (e.target.closest(".tt-drag-handle")) return;
      if (_tooltipDragging) return;
      window.location.href = "/topic/" + d.id + "/overview";
    };
  }

  function deselectNode() {
    selectedNode = null;
    nodeSel.attr("opacity", 1);
    linkSel.attr("stroke", "#444").attr("stroke-opacity", 0.5)
      .attr("stroke-width", 1.5).attr("marker-end", "url(#arrowhead)");
    hideTooltip();
  }

  // Click SVG background to deselect
  svg.on("click", (event) => {
    if (!selectedNode) return;
    if (_tooltipDragging) return;
    deselectNode();
  });

  // ── Draggable tooltip ──────────────────────────────────────────────────────
  let _tooltipDragOffset = { x: 0, y: 0 };
  (function initDraggableTooltip() {
    let handle = tooltip.querySelector(".tt-drag-handle");
    if (!handle) {
      handle = document.createElement("div");
      handle.className = "tt-drag-handle";
      handle.innerHTML = "⠿";
      tooltip.prepend(handle);
    }
    handle.addEventListener("mousedown", startDrag);
    handle.addEventListener("touchstart", startDrag, { passive: false });

    function startDrag(e) {
      e.preventDefault(); e.stopPropagation();
      _tooltipDragging = true;
      const rect = tooltip.getBoundingClientRect();
      const cx = e.touches ? e.touches[0].clientX : e.clientX;
      const cy = e.touches ? e.touches[0].clientY : e.clientY;
      _tooltipDragOffset.x = cx - rect.left;
      _tooltipDragOffset.y = cy - rect.top;
      document.addEventListener("mousemove", onDrag);
      document.addEventListener("mouseup", endDrag);
      document.addEventListener("touchmove", onDrag, { passive: false });
      document.addEventListener("touchend", endDrag);
    }
    function onDrag(e) {
      if (!_tooltipDragging) return;
      e.preventDefault();
      const cx = e.touches ? e.touches[0].clientX : e.clientX;
      const cy = e.touches ? e.touches[0].clientY : e.clientY;
      tooltip.style.left = (cx - _tooltipDragOffset.x) + "px";
      tooltip.style.top = (cy - _tooltipDragOffset.y) + "px";
    }
    function endDrag() {
      document.removeEventListener("mousemove", onDrag);
      document.removeEventListener("mouseup", endDrag);
      document.removeEventListener("touchmove", onDrag);
      document.removeEventListener("touchend", endDrag);
      setTimeout(() => { _tooltipDragging = false; }, 50);
    }
  })();

  // ── Target add/remove ─────────────────────────────────────────────────────
  function toggleTarget(topicId, add) {
    const url = add ? "/api/targets/add" : "/api/targets/remove";
    fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ topic_id: topicId })
    }).then(r => r.json()).then(data => {
      if (data.ok) {
        if (add) userTargets.add(topicId);
        else userTargets.delete(topicId);
        // Update button text
        const btn = document.getElementById("tt-target-btn");
        if (btn) {
          if (userTargets.has(topicId)) {
            btn.textContent = "✕ Remove Target";
            btn.onclick = (e) => { e.stopPropagation(); toggleTarget(topicId, false); };
          } else {
            btn.textContent = "🎯 Add Target";
            btn.onclick = (e) => { e.stopPropagation(); toggleTarget(topicId, true); };
          }
        }
      }
    });
  }

  // ── Drag ────────────────────────────────────────────────────────────────────
  function drag(sim) {
    return d3.drag()
      .on("start", (event, d) => {
        if (!event.active) sim.alphaTarget(0.3).restart();
        d.fx = d.x; d.fy = d.y;
      })
      .on("drag", (event, d) => { d.fx = event.x; d.fy = event.y; })
      .on("end", (event, d) => {
        if (!event.active) sim.alphaTarget(0);
        d.fx = null; d.fy = null;
      });
  }

  // ── Search filter ────────────────────────────────────────────────────────────
  document.getElementById("graph-search").addEventListener("input", function () {
    const q = this.value.trim().toLowerCase();
    if (!q) {
      nodeSel.attr("opacity", 1);
      linkSel.attr("stroke-opacity", 0.5);
      return;
    }
    const matching = new Set(allNodes.filter(n =>
      n.name.toLowerCase().includes(q) ||
      n.level.toLowerCase().includes(q) ||
      n.tagline.toLowerCase().includes(q)
    ).map(n => n.id));

    nodeSel.attr("opacity", d => matching.has(d.id) ? 1 : 0.08);
    linkSel.attr("stroke-opacity", l => {
      const s = l.source.id || l.source;
      const t = l.target.id || l.target;
      return (matching.has(s) && matching.has(t)) ? 0.6 : 0.04;
    });
  });

  // ── Level filter ─────────────────────────────────────────────────────────────
  document.getElementById("level-filter").addEventListener("change", function () {
    const level = this.value;
    if (level === "all") {
      nodeSel.attr("opacity", 1);
      linkSel.attr("stroke-opacity", 0.5);
      return;
    }
    const matching = new Set(allNodes.filter(n => n.level === level).map(n => n.id));
    nodeSel.attr("opacity", d => matching.has(d.id) ? 1 : 0.08);
    linkSel.attr("stroke-opacity", l => {
      const s = l.source.id || l.source;
      const t = l.target.id || l.target;
      return matching.has(s) || matching.has(t) ? 0.4 : 0.04;
    });
  });

  // ── Reset zoom ───────────────────────────────────────────────────────────────
  document.getElementById("reset-zoom-btn").addEventListener("click", () => {
    svg.transition().duration(500).call(zoom.transform, d3.zoomIdentity.translate(W / 4, H / 4).scale(0.7));
  });

  // Initial zoom out to show full graph
  svg.call(zoom.transform, d3.zoomIdentity.translate(W * 0.05, H * 0.05).scale(0.65));

  // ── Legend click — highlight that level's nodes (no zoom) ────────────────────
  let activeLegendLevel = null;

  // Each node <g> gets a "halo" circle sitting behind the main circle.
  // We add it once to every node and keep it invisible until needed.
  nodeSel.insert("circle", "circle")   // insert BEFORE the main circle so it sits behind
    .attr("class", "node-halo")
    .attr("r", 0)
    .attr("fill", "none")
    .attr("stroke", "#FFD700")
    .attr("stroke-width", 3)
    .attr("stroke-opacity", 0)
    .attr("filter", "url(#halo-blur)");

  // Blur filter for the glow effect
  const defs = svg.select("defs");
  const filter = defs.append("filter")
    .attr("id", "halo-blur")
    .attr("x", "-50%").attr("y", "-50%")
    .attr("width", "200%").attr("height", "200%");
  filter.append("feGaussianBlur")
    .attr("in", "SourceGraphic")
    .attr("stdDeviation", "4");

  window.legendClick = function(el) {
    const level = el.dataset.level;

    // Toggle off if clicking the same legend item again
    if (activeLegendLevel === level) {
      legendReset();
      return;
    }
    activeLegendLevel = level;

    // Update legend chip styles
    document.querySelectorAll('.legend-item[data-level]').forEach(function(item) {
      item.classList.toggle('legend-active', item.dataset.level === level);
      item.classList.toggle('legend-dimmed', item.dataset.level !== level);
    });
    document.getElementById('legend-reset').style.display = 'flex';

    // Sync the dropdown filter
    const filterSel = document.getElementById('level-filter');
    if (filterSel) filterSel.value = level;

    const matching = new Set(allNodes.filter(n => n.level === level).map(n => n.id));

    // ── Dim non-matching nodes ──
    nodeSel.transition().duration(300)
      .attr("opacity", d => matching.has(d.id) ? 1 : 0.10);

    // ── Main circle: enlarge matching nodes ──
    nodeSel.select("circle.node-circle").transition().duration(300)
      .attr("r",            d => matching.has(d.id) ? (d.complete ? 30 : 26) : (d.complete ? 20 : 16))
      .attr("stroke-width", d => matching.has(d.id) ? 3 : (d.complete ? 3 : 2))
      .attr("stroke",       d => matching.has(d.id) ? "#fff"  : (d.complete ? "#fff" : d.color));

    // ── Halo ring: animate in on matching nodes ──
    nodeSel.select("circle.node-halo").transition().duration(300)
      .attr("r",             d => matching.has(d.id) ? (d.complete ? 38 : 34) : 0)
      .attr("stroke-opacity",d => matching.has(d.id) ? 0.85 : 0)
      // Pulse: second transition on top
      .on("end", function(d) {
        if (!matching.has(d.id)) return;
        d3.select(this)
          .transition().duration(700).ease(d3.easeSinInOut)
          .attr("r", d.complete ? 42 : 38)
          .attr("stroke-opacity", 0.4)
          .transition().duration(700).ease(d3.easeSinInOut)
          .attr("r", d.complete ? 38 : 34)
          .attr("stroke-opacity", 0.85)
          .on("end", function(d2) {
            if (activeLegendLevel === level) {
              d3.select(this).dispatch("end");
            }
          });
      });

    // ── Label text: larger + bold for matching nodes ──
    nodeSel.select("text.node-label").transition().duration(300)
      .attr("font-size",   d => matching.has(d.id) ? "13px" : "9px")
      .attr("font-weight", d => matching.has(d.id) ? "bold"  : "normal")
      .attr("fill",        d => matching.has(d.id) ? "#fff"  : "#ccc")
      .attr("dy",          d => matching.has(d.id) ? "38px"  : "30px");

    // ── Zoom to fit matching nodes ──
    const matchingNodes = allNodes.filter(n => matching.has(n.id));
    if (matchingNodes.length > 0) {
      const xs = matchingNodes.map(n => n.x);
      const ys = matchingNodes.map(n => n.y);
      const minX = Math.min(...xs), maxX = Math.max(...xs);
      const minY = Math.min(...ys), maxY = Math.max(...ys);
      const padX = 140, padY = 120;
      const bw = maxX - minX + padX * 2;
      const bh = maxY - minY + padY * 2;
      const scale = Math.min(W / bw, H / bh, 2.5);
      const tx = W / 2 - scale * (minX + maxX) / 2;
      const ty = H / 2 - scale * (minY + maxY) / 2;
      svg.transition().duration(650)
        .call(zoom.transform, d3.zoomIdentity.translate(tx, ty).scale(scale));
    }

    // ── Dim links ──
    linkSel.transition().duration(300)
      .attr("stroke",         l => {
        const s = l.source.id || l.source;
        const t = l.target.id || l.target;
        return (matching.has(s) && matching.has(t)) ? "#FFD700" : "#444";
      })
      .attr("stroke-opacity", l => {
        const s = l.source.id || l.source;
        const t = l.target.id || l.target;
        return (matching.has(s) && matching.has(t)) ? 0.7 : 0.04;
      })
      .attr("stroke-width", l => {
        const s = l.source.id || l.source;
        const t = l.target.id || l.target;
        return (matching.has(s) && matching.has(t)) ? 2.5 : 1;
      });
  };

  window.legendReset = function() {
    activeLegendLevel = null;
    document.querySelectorAll('.legend-item[data-level]').forEach(function(item) {
      item.classList.remove('legend-active', 'legend-dimmed');
    });
    document.getElementById('legend-reset').style.display = 'none';
    const filterSel = document.getElementById('level-filter');
    if (filterSel) filterSel.value = 'all';

    // Restore all nodes
    nodeSel.transition().duration(300).attr("opacity", 1);

    nodeSel.select("circle.node-circle").transition().duration(300)
      .attr("r",            d => d.complete ? 20 : 16)
      .attr("stroke-width", d => d.complete ? 3 : 2)
      .attr("stroke",       d => d.complete ? "#fff" : d.color);

    // Hide all halos
    nodeSel.select("circle.node-halo").transition().duration(200)
      .attr("r", 0)
      .attr("stroke-opacity", 0);

    // Restore label text
    nodeSel.select("text.node-label").transition().duration(300)
      .attr("font-size",   "9px")
      .attr("font-weight", "normal")
      .attr("fill",        "#ccc")
      .attr("dy",          "30px");

    // Restore links
    linkSel.transition().duration(300)
      .attr("stroke", "#444")
      .attr("stroke-opacity", 0.5)
      .attr("stroke-width", 1.5)
      .attr("marker-end", "url(#arrowhead)");

    // Reset zoom to overview
    svg.transition().duration(500)
      .call(zoom.transform, d3.zoomIdentity.translate(W * 0.05, H * 0.05).scale(0.65));
  };

  // ── Helpers ──────────────────────────────────────────────────────────────────
  function truncate(str, n) {
    return str.length > n ? str.slice(0, n - 1) + "…" : str;
  }

})();
