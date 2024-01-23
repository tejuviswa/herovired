import psutil
import time
import msvcrt  # For Windows-specific key detection


def monitor_cpu(threshold=80):
    """
    Continuously monitor CPU usage and display alerts if it exceeds a threshold.
    Stops monitoring when any key is pressed.

    Args:
        threshold: The CPU usage threshold (percentage) to trigger an alert.
    """
    try:
        while True:
            cpu_usage = psutil.cpu_percent()
            print(f"Monitoring CPU usage: {cpu_usage:.2f}%")

            if cpu_usage > threshold:
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage:.2f}%")

            time.sleep(1)  # Adjust sleep interval as needed

            # Check for key press (Windows-specific implementation)
            if msvcrt.kbhit():
                msvcrt.getch()  # Consume the key press
                break
            

    except Exception as e:
        print(f"Error during monitoring: {e}")


if __name__ == "__main__":
    monitor_cpu()
