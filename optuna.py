
study = optuna.create_study(direction='minimize')
study.optimize(objective, n_trials=600)


optuna.visualization.plot_optimization_history(study)
optuna.visualization.plot_slice(study)
optuna.visualization.plot_param_importances(study)


Best_trial=study.best_trial.params
fix_dict = {
        'iterations': 700,          
        'depth': 3,
        'border_count': 88,         
        'verbose': False,
  }
Best_trial.update(fix_dict)

#############################

optuna.logging.set_verbosity(optuna.logging.ERROR)

# Optunaの冗長レベルを「ERROR」に設定します。
# ほとんどのログメッセージが抑制されます。
