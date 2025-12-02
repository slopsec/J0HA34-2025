```
Find <-- 7
Found <-- False
Start <-- 0
End <-- length(list)

WHILE Found = False AND Start <= End
     Mid <-- (Start + End) DIV 2

     IF list[Mid] = Find THEN
        OUTPUT 'Found at' +  Mid
        Found <-- True
     ELSE
        IF List[Mid] > Find THEN
           End <-- Mid - 1
        ELSE
          Start <-- Mid + 1
        ENDIF
     ENDIF
ENDWHILE

IF Found = False THEN
     OUTPUT 'Not found'
ENDIF
```