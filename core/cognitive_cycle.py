import threading
import time


class CognitiveCycle:

    def __init__(self, brain, interval=30):

        self.brain = brain
        self.interval = interval

        self.running = False
        self.thread = None

    def start(self):

        if self.running:
            return

        self.running = True

        self.thread = threading.Thread(
            target=self.loop,
            daemon=True
        )

        self.thread.start()

    def stop(self):

        self.running = False

        if self.thread:
            self.thread.join(timeout=1)

    def loop(self):

        while self.running:

            try:

                self.step()

            except Exception as e:

                print(f"[CognitiveCycle] {e}")

            time.sleep(self.interval)

    def step(self):

        # Execute one queued task

        if hasattr(self.brain, "executive"):

            try:
                self.brain.executive.execute_next()
            except Exception:
                pass

        # Periodic memory save

        if hasattr(self.brain, "episode"):

            try:
                if hasattr(self.brain.episode, "save"):
                    self.brain.episode.save()
            except Exception:
                pass
            
        # Semantic memory save

        if hasattr(self.brain, "semantic"):

            try:
                if hasattr(self.brain.semantic, "save"):
                    self.brain.semantic.save()
            except Exception:
                pass

        # Future scheduler hook

        if hasattr(self.brain, "scheduler"):

            try:
                self.brain.scheduler.run_pending()
            except Exception:
                pass