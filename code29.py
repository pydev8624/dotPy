def outer():
    def inner():
        print("سلام از تابع داخلی")
    inner()

outer()
