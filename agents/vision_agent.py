import os

from vision.vision_engine import VisionEngine


class VisionAgent:


    def __init__(self):

        self.engine = VisionEngine()

        self.last_result = None

    # -------------------------------------------------

    def analyze(self, image_path):

        if not os.path.exists(image_path):

            return {
                "success": False,
                "error": "Image not found."
            }

        try:

            result = self.engine.analyze(image_path)

            self.last_result = result

            return {
                "success": True,
                "result": result
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }

    # -------------------------------------------------

    def caption(self, image_path):

        data = self.analyze(image_path)

        if not data["success"]:

            return None

        result = data["result"]

        if isinstance(result, dict):

            return result.get("caption")

        return None

    # -------------------------------------------------

    def objects(self, image_path):

        data = self.analyze(image_path)

        if not data["success"]:

            return []

        result = data["result"]

        if isinstance(result, dict):

            return result.get("objects", [])

        return []

    # -------------------------------------------------

    def ocr(self, image_path):

        data = self.analyze(image_path)

        if not data["success"]:

            return ""

        result = data["result"]

        if isinstance(result, dict):

            return result.get("text", "")

        return ""

    # -------------------------------------------------

    def scene(self, image_path):

        data = self.analyze(image_path)

        if not data["success"]:

            return None

        result = data["result"]

        if isinstance(result, dict):

            return result.get("scene")

        return None

    # -------------------------------------------------

    def last_analysis(self):

        return self.last_result

    # -------------------------------------------------

    def summary(self):

        if not self.last_result:

            return "No image has been analyzed."

        result = self.last_result

        lines = []

        caption = result.get("caption")

        if caption:
            lines.append(f"Caption : {caption}")

        scene = result.get("scene")

        if scene:
            lines.append(f"Scene   : {scene}")

        objects = result.get("objects")

        if objects:
            lines.append(
                "Objects : " +
                ", ".join(objects)
            )

        text = result.get("text")

        if text:
            lines.append(
                f"OCR      : {text}"
            )

        return "\n".join(lines)