import cricketlivescore
def livegetit():
     scores = cricketlivescore.get()
     line=""
     for score in scores:
          line=line+score.title+"\n"
     print(line)
     return line
