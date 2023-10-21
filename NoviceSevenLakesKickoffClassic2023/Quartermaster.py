totalmoney, totalcrew = input().split(" ")
crewmembers = []

for i in range(int(totalcrew)):
    name, role, shares = input().split(" ")
    crewmembers.append((name, role, int(shares)))

totalshares = sum(shares for _, _, shares in crewmembers)
tmps = int(totalmoney) / totalshares

print("| Name     | Role          | # of Shares | % of Total | Money   |")
print("| -------- | ------------- | ----------- | ---------- | ------- |")

for name, role, shares in crewmembers:
    percentage = (shares / totalshares) * 100
    money = tmps * shares
    shares>=1
    print(f"| {name:<8} | {role:<13} | {shares:<11} | {percentage:.2f}%     | ${money:.2f} |")

print(f"| Total    |               |             |            | ${int(totalmoney):.2f} |")

# fail - didn't output correctly (table wasn't correct sizing)
# didn't know how to dynamically resize a table, so I just tried to copy the output of the sample table
