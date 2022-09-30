from formations.app_executer import Executer

class AppExecuter:

    def __init__(self):
        self.executer = Executer()

    def run_application(self):
        self.executer.create_execution()
