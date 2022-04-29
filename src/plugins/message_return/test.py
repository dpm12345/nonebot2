
import re
str = "2这就是cyy"

if re.match("^这就是",str):
    print("success")
else:
    print("failed")