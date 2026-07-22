import threading
import time


class ThinkingLoop:

    def __init__(self, brain, interval=5):

        self.brain = brain
        self.interval = interval

        self.running = False
        self.thread = None

    # ---------------------------------

    def start(self):

        if self.running:
            return

        self.running = True

        self.thread = threading.Thread(
            target=self.loop,
            daemon=True
        )

        self.thread.start()

    # ---------------------------------

    def stop(self):

        self.running = False

        if self.thread:
            self.thread.join(timeout=1)

    # ---------------------------------

    def loop(self):

        while self.running:

            try:

                self.background_tasks()

            except Exception as e:

                print(f"[ThinkingLoop] {e}")

            time.sleep(self.interval)

    # ---------------------------------

    def background_tasks(self):

        if hasattr(self.brain, "executive"):

            try:

                self.brain.executive.execute_next()

            except Exception as e:

                print(f"[Executive] {e}")

        if hasattr(self.brain, "scheduler"):

            try:

                self.brain.scheduler.run_pending()

            except Exception:
                pass