TITLE = "MSE and Regression Losses"

SECTIONS = [
    {
        "id": "reg_mse",
        "title": "Mean Squared Error (MSE)",
        "body": "MSE is the standard loss for regression tasks. Formula: L = (1/N) * sum((y_i - y_hat_i)^2). It penalizes large errors quadratically, making it sensitive to outliers. MSE is differentiable and convex, enabling efficient optimization with gradient descent."
    },
    {
        "id": "reg_mae",
        "title": "Mean Absolute Error (MAE)",
        "body": "MAE measures average absolute deviations: L = (1/N) * sum(|y_i - y_hat_i|). Unlike MSE, MAE is robust to outliers because it penalizes errors linearly. However, MAE is not differentiable at zero, making optimization slightly more complex. Use MAE when outliers are problematic."
    },
    {
        "id": "reg_huber",
        "title": "Huber Loss: Balanced Approach",
        "body": "Huber loss combines MSE and MAE properties. It is quadratic for small errors (like MSE) and linear for large errors (like MAE). This makes it robust to outliers while maintaining smooth gradients. It requires a hyperparameter delta that sets the transition point."
    },
    {
        "id": "reg_mape",
        "title": "Mean Absolute Percentage Error (MAPE)",
        "body": "MAPE measures percentage errors: L = (1/N) * sum(|y_i - y_hat_i| / |y_i|). Useful for data with different scales. MAPE is scale-invariant and interpretable as a percentage. Avoid when true values are near zero to prevent division issues."
    }
]
