a = {
    "name" : "pnimfosys,",
    "collage" : "rjit",
    #"college":"itm",
    "mark" : [1,2,3,4],
    "education":{'ram':'mca'},
    1:2,

}
#print(a["college78"])
# print(a.get("college"))
# print(a.key())
# print(type(a.keys()))
# print(a.values())

updatedict= {
    "branch" : "it",
    "phone" :9823293729,
    "salary" : 4000,
    "name" : "rohit"

}
a.update(updatedict)
print(a)
#----------------------------
try:
    print(a["college122"])
except Exception as e:
    print(e)
print(a["collage"])    