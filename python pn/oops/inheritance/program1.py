# class c2devc:
#     def __init__(self, i, j):
#         self.icap = i
#         self.jcap = j

#     def __str__(self):
#         return f"{self.icap}i + {self.jcap}j"  
# class c3devc(c2devc):
#     def __init__(self, i, j ,k):
#         super().__init__(i,j)
#         self.kcap = K
#     def __str__(Self):
#         return f"{self.icap}i + {self.jcap}j + {self.jcap}k"

# v2d = c2devc(1,3) 
# v3d = c3devc(1, 9, 7)

# print(v2d)
# print(v3d)

class c2devc:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"


class c3devc(c2devc):
    def __init__(self, i, j, k):
        super().__init__(i, j)   # only i, j
        self.kcap = k            # correct variable

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"


v2d = c2devc(1, 3)
v3d = c3devc(1, 9, 7)

print(v2d)
print(v3d)