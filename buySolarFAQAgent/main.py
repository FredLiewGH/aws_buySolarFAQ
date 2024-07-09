from InvokeAgent.Common.Logging import CustomLogger
from InvokeAgent.Modules.Converse import startChat
from datetime import datetime

# Main script 
if __name__ == '__main__':
    logdate = str(datetime.today().strftime('%Y%m%d'))
    logger = CustomLogger(f"D:\\Source\\Python\\Logs", f"{logdate}_buySolarFAQAgent.txt") 
    startChat(logger)
