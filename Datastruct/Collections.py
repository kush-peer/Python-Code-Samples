from collections import defaultdict
import json
def main():
     print("Fun executed")

# default dictionery
def defaultColl():
    colors =(("green", "blue"),
        ("red", "yellow"),
        ("blue", "green"))
    fav_colors = defaultdict(list)

    tree= lambda: defaultdict(tree)
    some_dic = tree()
    some_dic['color']['red'] = 'yellow'
    print(json.dumps(some_dic))
    for name, color in colors:
        fav_colors[name].append(color)
    return fav_colors



fav_colors = defaultColl()
print(fav_colors)
  
if __name__ == "__main__":
    main()