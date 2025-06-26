import shutil

usage = shutil.disk_usage('C:\\')

print("Total: {:.2f} GB\nUsed: {:.2f} GB\nFree: {:.2f} GB".format(
    usage.total / 1024 / 1024 / 1024,
    usage.used / 1024 / 1024 / 1024,
    usage.free / 1024 / 1024 / 1024
))
