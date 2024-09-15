set.seed(123)
n_sims <- 1000  # Number of simulations
target_power <- 0.80  # Target power
effect_size <- find_value(dir = 'min', LHB_lowereff, CPP_lowereff)  # True effect size (mean difference)
alpha <- result$par[1]
beta <- result$par[2]
n <- 2  # Initial sample size

power_at_n <- numeric()  # Store power for each sample size
cohens_ds_at_n <- numeric()  # Store mean Cohen's d for each sample size

while(TRUE) {
  p_vals <- numeric(n_sims)  # Preallocate p-value storage
  cohens_ds <- numeric(n_sims)  # Preallocate Cohen's d storage
  
  for(sim in 1:n_sims) {
    difference <- rbeta(n, shape1 = alpha, shape2 = beta)  # Simulate the difference scores
    t_test_result <- t.test(difference, mu = 0)  # Run t-test
    p_vals[sim] <- t_test_result$p.value  # Extract p-value
    d <- effectsize::t_to_d(
      t = as.numeric(t_test_result$statistic), 
      df_error = n - 1, paired = TRUE)$d   # Calculate Cohen's d
    cohens_ds[sim] <- as.numeric(d)
  }
  print(d)

  # Calculate power and mean Cohen's d for current sample size
  power_at_n <- c(power_at_n, mean(p_vals < alpha))
  print(power_at_n)
  cohens_ds_at_n <- c(cohens_ds_at_n, mean(cohens_ds))
  
  # Check if the target power has been achieved
  if (power_at_n[length(power_at_n)] >= target_power) {
    break
  }
  
  n <- n + 1  # Increase sample size
}

