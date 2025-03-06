

def evaluate_multiple_episodes(model, num_episodes=10, max_angle_degrees=6.0, max_position=2.4, 
                              max_steps=200, seed=42, render_last=True):
    """
    Evaluates a trained model over multiple episodes and tracks performance metrics.
    
    Parameters:
    model: Trained model (must have a predict function)
    num_episodes: Number of episodes to run
    max_angle_degrees: Maximum allowable angle (in degrees)
    max_position: Maximum allowable position
    max_steps: Maximum number of steps per episode
    seed: Initial random seed (will be incremented for each episode)
    render_last: Whether to render the last episode
    
    Returns:
    dict: Performance metrics and visualization data for the last episode
    """
    # Initialize metrics storage
    episode_lengths = []
    episode_rewards = []
    episode_termination_reasons = []
    
    # For visualization of the last episode
    last_episode_data = None
    
    print(f"Evaluating model over {num_episodes} episodes...")
    
    for episode in range(num_episodes):
        current_seed = seed + episode  # Different seed for each episode
        
        # Run a single evaluation episode
        observations, rewards, total_reward, termination_reason = evaluate_model_with_custom_env(
            model, 
            max_angle_degrees=max_angle_degrees, 
            max_position=max_position,
            max_steps=max_steps, 
            seed=current_seed
        )
        
        # Record metrics
        episode_length = len(observations) - 1  # Subtract 1 for initial observation
        episode_lengths.append(episode_length)
        episode_rewards.append(total_reward)
        episode_termination_reasons.append(termination_reason)
        
        # Progress update
        print(f"Episode {episode+1}/{num_episodes}: Steps={episode_length}, " +
              f"Reward={total_reward:.2f}, Reason='{termination_reason}'")
        
        # Save data for the last episode for visualization
        if episode == num_episodes - 1:
            last_episode_data = (observations, rewards, total_reward, termination_reason)
    
    # Calculate summary statistics
    avg_length = sum(episode_lengths) / num_episodes
    avg_reward = sum(episode_rewards) / num_episodes
    max_reward = max(episode_rewards)
    
    # Count termination reasons
    reason_counts = {}
    for reason in episode_termination_reasons:
        if reason in reason_counts:
            reason_counts[reason] += 1
        else:
            reason_counts[reason] = 1
    
    # Print summary
    print("\n--- Evaluation Summary ---")
    print(f"Average episode length: {avg_length:.2f} steps")
    print(f"Average episode reward: {avg_reward:.2f}")
    print(f"Maximum episode reward: {max_reward:.2f}")
    print("Termination reasons:")
    for reason, count in reason_counts.items():
        print(f"  - {reason}: {count} episodes ({count/num_episodes*100:.1f}%)")
    
    # Render the last episode if requested
    if render_last and last_episode_data:
        print("\nVisualizing last episode...")
        animate_cartpole(*last_episode_data)
    
    # Return results
    return {
        "episode_lengths": episode_lengths,
        "episode_rewards": episode_rewards,
        "episode_termination_reasons": episode_termination_reasons,
        "avg_length": avg_length,
        "avg_reward": avg_reward,
        "max_reward": max_reward,
        "last_episode_data": last_episode_data
    }

# Function to plot learning progress
def plot_learning_progress(results, window_size=5):
    """
    Plots the learning progress over multiple evaluation runs.
    
    Parameters:
    results: List of evaluation results from evaluate_multiple_episodes() calls
    window_size: Size of the rolling average window
    """
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.ticker import MaxNLocator
    
    # Extract data for plotting
    evaluation_points = []
    episode_rewards = []
    episode_lengths = []
    avg_rewards = []
    avg_lengths = []
    max_rewards = []
    
    for i, result in enumerate(results):
        evaluation_points.extend([i] * len(result["episode_rewards"]))
        episode_rewards.extend(result["episode_rewards"])
        episode_lengths.extend(result["episode_lengths"])
        avg_rewards.append(result["avg_reward"])
        avg_lengths.append(result["avg_length"])
        max_rewards.append(result["max_reward"])
    
    # Create a figure with 2 subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Plot scatter of individual episode rewards
    ax1.scatter(evaluation_points, episode_rewards, alpha=0.3, color='blue', label='Episode Rewards')
    
    # Plot average reward over evaluations
    x_points = list(range(len(results)))
    ax1.plot(x_points, avg_rewards, 'r-', linewidth=2, label='Average Reward')
    ax1.plot(x_points, max_rewards, 'g-', linewidth=2, label='Max Reward')
    
    # Calculate rolling average if we have enough data
    if len(episode_rewards) >= window_size:
        # Create pairs of (evaluation_point, reward)
        data_pairs = list(zip(evaluation_points, episode_rewards))
        # Sort by evaluation point
        data_pairs.sort()
        
        # Extract sorted data
        sorted_x = [p[0] for p in data_pairs]
        sorted_rewards = [p[1] for p in data_pairs]
        
        # Compute rolling average
        rolling_rewards = []
        for i in range(len(sorted_rewards) - window_size + 1):
            rolling_rewards.append(sum(sorted_rewards[i:i+window_size]) / window_size)
        
        rolling_x = sorted_x[window_size-1:]
        ax1.plot(rolling_x, rolling_rewards, 'k--', linewidth=1.5, 
                label=f'Rolling Avg (window={window_size})')
    
    # Set up reward plot
    ax1.set_xlabel('Evaluation Point')
    ax1.set_ylabel('Reward')
    ax1.set_title('Reward Over Learning Progress')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
    
    # Plot episode lengths
    ax2.scatter(evaluation_points, episode_lengths, alpha=0.3, color='purple', label='Episode Length')
    ax2.plot(x_points, avg_lengths, 'r-', linewidth=2, label='Average Length')
    
    # Calculate rolling average for lengths if we have enough data
    if len(episode_lengths) >= window_size:
        # Create pairs of (evaluation_point, length)
        data_pairs = list(zip(evaluation_points, episode_lengths))
        # Sort by evaluation point
        data_pairs.sort()
        
        # Extract sorted data
        sorted_x = [p[0] for p in data_pairs]
        sorted_lengths = [p[1] for p in data_pairs]
        
        # Compute rolling average
        rolling_lengths = []
        for i in range(len(sorted_lengths) - window_size + 1):
            rolling_lengths.append(sum(sorted_lengths[i:i+window_size]) / window_size)
        
        rolling_x = sorted_x[window_size-1:]
        ax2.plot(rolling_x, rolling_lengths, 'k--', linewidth=1.5, 
                label=f'Rolling Avg (window={window_size})')
    
    # Set up length plot
    ax2.set_xlabel('Evaluation Point')
    ax2.set_ylabel('Episode Length (steps)')
    ax2.set_title('Episode Length Over Learning Progress')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.xaxis.set_major_locator(MaxNLocator(integer=True))
    
    plt.tight_layout()
    plt.show()
    
    return fig

# Example usage:
# For evaluating during training
def evaluate_during_training(model, training_steps, eval_frequency=10000, num_episodes=10):
    """
    Evaluates the model periodically during training and tracks progress.
    
    Parameters:
    model: The model being trained (must have a predict method)
    training_steps: Total number of training steps to perform
    eval_frequency: How often to evaluate (in training steps)
    num_episodes: Number of episodes to run per evaluation
    
    Returns:
    list: List of evaluation results at each checkpoint
    """
    evaluation_results = []
    
    for step in range(0, training_steps + 1, eval_frequency):
        # Assuming you can get the model at the current training step
        # This might need to be adapted to your specific training loop
        print(f"\n--- Evaluating model at {step} training steps ---")
        
        # Evaluate model
        result = evaluate_multiple_episodes(
            model, 
            num_episodes=num_episodes, 
            render_last=(step == training_steps)  # Only render on the last evaluation
        )
        
        # Store results
        evaluation_results.append(result)
        
        # Optionally plot progress so far
        if len(evaluation_results) > 1:
            plot_learning_progress(evaluation_results)
        
        # Continue training...
        # (Your training code here)
    
    return evaluation_results

# Perform multiple evaluations of a single model
def evaluate_training_progress(model, num_evaluation_sets=3, episodes_per_evaluation=5):
    """
    Evaluate the current model multiple times to track progress.
    
    Parameters:
    model: The trained model to be evaluated
    num_evaluation_sets: Number of evaluation sets to run
    episodes_per_evaluation: Number of episodes to run per evaluation set
    
    Returns:
    list: A list of results from each evaluation set
    """
    results = []
    
    for eval_set in range(num_evaluation_sets):
        print(f"\nRunning evaluation set {eval_set+1}/{num_evaluation_sets}...")

        # Evaluate the model
        result = evaluate_multiple_episodes(
            model, 
            num_episodes=episodes_per_evaluation,
            seed=42 + (eval_set * 100)  # Use different seed values for each evaluation set
        )

        results.append(result)

        # Display progress so far
        print(f"Average reward for evaluation set {eval_set+1}: {result['avg_reward']:.2f}")
        print(f"Average episode length for evaluation set {eval_set+1}: {result['avg_length']:.2f}")
    
    # Compute overall averages across all evaluations
    all_rewards = []
    all_lengths = []
    
    for result in results:
        all_rewards.extend(result["episode_rewards"])
        all_lengths.extend(result["episode_lengths"])
    
    overall_avg_reward = sum(all_rewards) / len(all_rewards) if all_rewards else 0
    overall_avg_length = sum(all_lengths) / len(all_lengths) if all_lengths else 0
    
    print("\n=== Overall Evaluation Summary ===")
    print(f"Overall average reward: {overall_avg_reward:.2f}")
    print(f"Overall average episode length: {overall_avg_length:.2f}")
    
    # Plot learning progress across evaluation sets
    if len(results) > 1:
        plot_learning_progress(results)
    
    return results

# During training
results = evaluate_during_training(model, training_steps=10000, eval_frequency=1000)


# Visualize learning progress
plot_learning_progress(results)


# This only uses the current model (no checkpoints needed)
evaluation_results = evaluate_training_progress(model, num_evaluation_sets=5, episodes_per_evaluation=5)
