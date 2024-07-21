if(haystack==needle) :
    return 0
if(needle not in haystack ) :
    return -1
if(needle  in haystack) :
for i in range(len(haystack)):
    if(haystack[i:i+len(needle)]==needle) :
        return i

return -1
