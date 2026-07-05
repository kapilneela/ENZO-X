class Plugin:

    def run(self, text):

        try:

            if "+" in text:

                nums = text.split("+")

                a = float(nums[0])

                b = float(nums[1])

                return str(a+b)

        except:

            pass

        return None