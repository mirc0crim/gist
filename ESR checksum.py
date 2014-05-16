test = {"93865900000000000007518299": 6}
test["93865900000000000007134804"] = 2
test["0000800305450002"] = 7
test["313947143000901"] = 8
test["0"] = 1 # test the detection of a wrong number

c = "0946827135"

for t in test:
    uber = 0
    for i in range(len(t)):
        uber = int(c[(int(t[i])+uber)%10])
    chsm = (10-uber)%10
    print("reference number:", t)
    print("expected:", test[t], "calculated", chsm)
    print(["-> not" if not chsm==test[t] else ""][0], "correct")
