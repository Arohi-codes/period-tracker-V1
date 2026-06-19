print("PERIOD TRACKER")
period_history = []
while True:
    print("1. add entry")
    print("2. view history")
    print("3. exit")
    choice = int(input("choose any option: "))
    if choice == 1:
        date = input("enter period start date: ")
        cramps = int(input("rate cramps [1-10]: "))
        flow = input("flow (light/medium/heavy): ")
        mood = input("enter your mood: ")
        cycle_length = int(input("enter cycle length (days): "))
        entry = {
            "date": date,
            "cramps": cramps,
            "flow": flow,
            "mood": mood,
            "cycle_length": cycle_length
        }
        period_history.append(entry)
        print("entry saved!")
    elif choice == 2:
        print("period tracker")
        if len(period_history) == 0:
            print("no entries found")
        else:
            for entry in period_history:
                print("==============")
                print("date:", entry["date"])
                print("cramps:", entry["cramps"])
                print("flow:", entry["flow"])
                print("mood:", entry["mood"])
                print("cycle_lenth:", entry["cycle_length"])
    elif choice == 3:
        print("okieee!! byee see you again!!")
        break
            