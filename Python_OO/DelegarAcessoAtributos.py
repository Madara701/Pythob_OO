class A:
    def fazer_algo(self):
        print("Palmeiras")
    def outro(self):
        print("campeão")

class B:
    def __init__(self):
        self.a = A()
    def fazer_algo(self):
        #delega para self.a
        return self.a.fazer_algo()
    def outro(self):
        #delegando novamente
        return self.a.outro()


b = B()
print(b.fazer_algo())
print(b.outro())

