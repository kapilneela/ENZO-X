class Tool:

    def run(self,data):

        try:

            return eval(data)

        except:

            return "Calculation failed"