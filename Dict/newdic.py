Allfight = {
   "UK" : {
       "2024-07-01" : {
         "12:30:00" : 20,
         "18:30:00" : 0,
         "21:30:00" : 100,
       },
       "2024-07-02" : {
         "12:30:00" : 20,
         "18:30:00" : 0,
         "21:30:00" : 100,
       }
   },
   "USA" : {
       "2024-08-01" : {
         "12:30:00" : 20,
         "18:30:00" : 0,
         "21:30:00" : 100,
       },
       "2024-08-02" : {
         "12:30:00" : 20,
         "18:30:00" : 0,
         "21:30:00" : 100,
       }
   }
}

# print Full dct
# print(Allfight)


# print specific part of dict
# print(Allfight["UK"])

#print specific first part of nested dict
print(Allfight["UK"]["2024-07-02"])

print(Allfight["UK"]["2024-07-02"]["21:30:00"])
    #  Allfight[destination][date][d]