class Search:

    def search(self, arr, ele):
        found = False
        for e in arr:
            if e == ele:
                found = True
        return found
