from datetime import datetime # this imports the date and time infromation
import csv  # This and below allows for a csv file to be created
from pathlib import Path
topspeed = {
    "topspeed1" : "Wickets × 4, 4 × Fly 30m, 2 × Fly 40m, 1 × 150m ",
    "topspeed2" : "Wickets × 4, 4 × Fly 30m, 2 × Fly 40m, 1 × 150m",
    "topspeed3" : "Wickets × 4, 4 × Fly 30m, 2 × Fly 40m, 2 × 80m"
}
accel = {
    "accel1" : "Wickets x 6, 4 × 20m starts, 4 × 30m starts, 3 × 60m",
    "accel2" : "Wickets × 6, 4 × 30m starts, 3 × 60m, 2 × Fly 30m, 1 × 120m",
    "accel3" : "Wickets × 6, 4 × 30m starts, 2 × 60m, 2 × Fly 30m, 1 × 150m"
}
tempoMF = {
    "tempoMF1" : "8 × 100m tempo",
    "tempoMF2" : "8 × 100m tempo",
    "tempoMF3" : "6 × 100m tempo"
}
tempoW = {
    "tempoW1" : "8 × 100m tempo",
    "tempoW2" : "8 × 100m tempo",
    "tempoW3" : "6 × 100m tempo"
}
endurance_by_week = {
    1: "None",
    2: "350 15min, 150 ",
    3: "300 15 min 250",
    5: "450",
    6: "300 15 min, 150 ",
    7: "500",
    8: "300 15 min 150",
    9: "2x300 12min ",
    11: "250 10 min, 120",
    12: "300m",
    13: "200m, 15 min, 150m ",
    14: "250m 15 min, 120m"
}
accellift = {
    "accellift1" : "Power Clean: 4 × 3 @ 75%, Back Squat: 4 × 5 @ 75%, RDL: 3 × 5 @ 75%, Pull-Ups: 3 × 8 Long-Lever, 2 × 25 sec, Heel-Dig 2 × 20sec, core",
    "accellift2" : "Power Clean: 4 × 3 @ 80%, Back Squat: 4 × 4 @ 80–85%, RDL: 3 × 5, Pull-Ups: 3 × 8, Core",
    "accellift3" : "Power Clean: 3 × 2 @ 85%, Back Squat: 5 × 3 @ 85%, RDL: 2 × 5"
}
topspeedlift = {
    "topspeedlift1" : "Power Clean: 3 × 2 @ 75%, Back Squat: 3 × 3 @ 75%, Box Jumps: 3 × 3, Bench Press: 3 × 5 @ 75%,Long-Lever, 2 × 25 sec Heel-Dig 2 × 20sec",
    "topspeedlift2" : "Power Clean: 3 × 2 @ 85%, Back Squat: 3 × 3 @ 85%, Box Jumps: 3 × 3, Bench Press: 3 × 4 @ 80%, Core",
    "topspeedlift3" : "Power Clean: 2 × 2 @ 80%, Back Squat: 2 × 3 @ 80%, Box Jumps: 2 × 3, Bench Press: 2 × 4 @ 75%, Core"
}
endurancelift = {
    "endurancelift1" : "Bulgarian Split Squat: 3 × 6 each leg, Bench Press: 3 × 5 @ 75–80%, Chin-Ups: 3 × 8, Nordic Hamstrings: tantrums 3x20s, Core",
    "endurancelift2" : "Bulgarian Split Squat: 3 × 5 each leg, Bench Press: 3 × 5 @ 75–80%, Chin-Ups: 3 × 8, Nordic Hamstrings: 3 × 5, Core",
    "endurancelift3" : "Bulgarian Split Squat: 2 × 5 each leg, Bench Press: 2 × 4, Chin-Ups: 2 × 8, Core"
}

hips_bad = """
Sore hips — bad

4 x 20 ankle pogos
3 x 20 both-feet over-line hops
20 side-to-side line hops
"""

hips_ok = """
Sore hips — ok

2 x easy stadium marches
Mobility + calf pulses
8 x single-step stadium runs @ 60–75%
Walk-down recovery
3 x 6 two-leg stadium hops
Isometrics
"""

hips_almost = """
Sore hips — almost

A. Rolling accelerations
4 x 20m rolling accelerations
Start with a 10m walk-in/jog-in
Accelerate from 60% to 80–85%
Full walk-back recovery

Rolling starts are better than static starts because they reduce the violent first-step hip/groin demand.

B. Hill or slight incline accelerations, if available
4 x 20m hill accelerations
70–80%
Smooth push, not sprinting
Walk-back recovery

A slight hill can be good because it naturally limits speed and keeps you from overstriding.
Do not drive aggressively or bound up the hill.

C. Short calf-stiffness finish
Pick 2–3:
Pogos: 3 x 15–20 sec
Ankling: 3 x 20m
Dribble runs: 2 x 20m
Straight-leg bounds, low amplitude only: 2 x 20m
Standing calf iso: 3 x 30–45 sec
Bent-knee soleus iso: 3 x 30–45 sec

Keep contacts quick and low. This gives you the calf/Achilles/foot stimulus without a large hip range.
"""


calves_bad = """
Sore calves — bad

5–8 min easy bike

Dynamic mobility:
Leg swings: 10 each
90/90s: 8 each
Glute bridges: 2 x 10
Dead bugs: 2 x 8 each

Bike workout:
10 min easy spin
2 sets of 5 x 10 sec fast-cadence bursts
50 sec easy spin between reps
4 min easy spin between sets
8–10 min cooldown

Effort: 75–85%
Resistance: low/moderate
Stay seated. No standing climbs.

Wall drills:
Wall marches: 2 x 10 each leg
Wall switches: 3 x 5 each leg
Wall drives: 4 x 5 sec
"""

calves_ok = """
Sore calves — ok

Bike primer:
6 x 10 sec fast cadence
50 sec easy spin between reps
Low/moderate resistance

This gives you turnover before running without needing hard contacts.

Controlled running replacement:
Instead of hard starts:
4 x 50–60m relaxed strides
60%, 65%, 70%, 75%

5 x 20m rolling accelerations
10m walk/jog-in
Accelerate to 75–80%

2–3 x 30m buildups
Smooth, max 80%

Full walk-back recovery.
"""

calves_almost = """
Sore calves — almost

Acceleration replacement:
Instead of 6 full strides:
4–5 x 60m progressive
65%, 75%, 80%, 85%, optional 85%

3 x 20m starts @ 80–85%
3 x 30m starts @ 80–85%
2 x 50–60m buildups @ 80–85%

Full recovery.
Stop if contacts get loud or calves tighten rep-to-rep.

Lower-leg stiffness:
Pogos: 2–3 x 15 sec
Ankling/dribble runs: 2–3 x 20m
Bent-knee soleus iso: 2 x 30 sec
Standing calf iso: 2 x 30 sec
"""


hamstrings_bad = """
Sore hamstring — bad

Goal:
Keep blood flow and mechanics without sprinting or elastic hamstring load.

Session:
10–15 min easy bike
Wall marches: 2 x 10 each
Wall switches: 2 x 5 each, slow/controlled
A-march: 2 x 20m
"""

hamstrings_ok = """
Sore hamstring — ok / mild soreness

Goal:
Reintroduce rhythm without high-speed hamstring demand.

Session:
5–8 min easy bike/jog
Dynamic mobility
Lighter warmup
4 x 50–60m strides @ 60–75%
4 x 20m rolling accelerations @ 70–75%
Ankling: 2 x 20m
Pogos: 2 x 15 sec
"""

hamstrings_almost = """
Sore hamstring — almost normal

Goal:
Get close to acceleration work without max hamstring stress.

Session:
Full warmup
4 x 60m progressive strides:
60%, 70%, 75%, 80%

5 x 20m rolling accelerations @ 75–85%
3 x 20m falling starts @ 75–80%
2 x 30m buildups @ 80%

Pogos: 2 x 15–20 sec
Ankling: 2 x 20m
Hamstring bridge iso: 2 x 30 sec
"""


core_bad = "rest"

core_ok = hips_bad

core_almost = hips_ok

quads_bad = """
Sore quads — bad

Warmup:
10–20 min easy bike
Resistance: low
Cadence: smooth, not grinding

Mobility / activation:
Leg swings: 10 each
90/90s: 8 each
Glute bridges: 2 x 10
Dead bugs: 2 x 8 each
Side plank: 2 x 25–30 sec each

Low-stress mechanics:
Wall marches: 2 x 10 each leg
Wall switches: 2 x 5 each leg
A-march: 2 x 20m, relaxed

Lower-leg maintenance:
Standing calf iso: 3 x 30 sec
Bent-knee soleus iso: 3 x 30 sec
Tib raises: 2 x 20
"""


quads_ok = """
Sore quads — ok

Warmup:
5–8 min easy bike or jog
Dynamic mobility
Glute bridges: 2 x 10
Calf pulses: 2 x 15
A-march: 2 x 20m

Strides:
4 x 50–60m progressive
60%, 65%, 70%, 75%

Acceleration substitute:
4 x 20m rolling accelerations
10m walk/jog-in
Build to 70–80%
Smooth, no hard push

2–3 x 30m buildups @ 70–80%

Low-depth plyo/stiffness:
Ankle pogos: 2–3 x 15 sec
Ankling: 2 x 20m
Standing calf iso: 2 x 30 sec
Bent-knee soleus iso: 2 x 30 sec
"""


quads_almost = """
Sore quads — almost normal

Strides:
4–5 x 60m progressive
60%, 70%, 75%, 80%, optional 85%

Acceleration:
4 x 20m rolling accelerations @ 80–85%
3 x 20m falling starts @ 75–85%
2–3 x 30m buildups @ 80–85%

Optional stiffness finish:
Pick 2:

Pogos: 3 x 15–20 sec
Ankling: 3 x 20m
Dribble runs: 2 x 20m, low amplitude
Standing calf iso: 3 x 30 sec
Bent-knee soleus iso: 3 x 30 sec
"""

indoor_accel_topspeed = """
Indoor replacement for acceleration / top speed

Progressive strides:
6 x 30m progressive strides
Rep 1: 60%
Rep 2: 65%
Rep 3: 70%
Rep 4: 75%
Rep 5: 80%
Rep 6: 85%

Short starts:
4 x 10m starts
Intensity: 85–90%
Rest: 60–90 sec

Acceleration starts:
4 x 20m starts
Intensity: 90–95%
Rest: 2–3 min

This replaces the original 4 x 20m starts well.

30m acceleration block:
8 x 25–30m starts
Intensity: 90–95%

Only go to 30m if you have enough room to shut down safely.
If deceleration space is tight, cap these at 25m.
"""


indoor_endurance = """
Indoor replacement for endurance

Treadmill workout:
3 rounds of:
60 sec on / 120 sec off
45 sec on / 90 sec off
30 sec on / 60 sec off

Progression options:
Option 1:
Speed: 7
Incline: 7

Option 2:
Speed: 8.5
Incline: 8.5

Option 3:
Speed: 10
Incline: 10
"""

mobility = """
Mobility

Hip flexor stretch
Hip flexor back stretch
Cat-cow
Child's pose
Glute figure-4 stretch
Glute hug
Hamstring floss
Hamstring stretch
Calf stretch, both calves
"""

foot_strength = """
Foot strength

Big toe raises: 2 x 10
Other toe raises: 2 x 10
Right ankle twists: 2 x 10
Left ankle twists: 2 x 10
Full-foot walks: 2 x 10
Calf pushes: 2 x 10
"""

core = """
Core

1. Dead bug, controlled
2–3 x 5–6 reps per side

2. Front plank, low dose
2 x 20–40 sec

3. Side plank, knees or feet
2 x 20–30 sec per side

4. Tim knee exercise
3 rounds

5. Copenhagen or butterfly
Copenhagen: controlled reps
or
Butterfly: 2 x 20

6. Glute bridge hold
2 x 20–30 sec

7. Reverse dead bugs
2 x 6
"""

hipshurdles = """
1. 2x leg over
2. 2x skip one
3. over unders
4. 90 90
5. 2x10 glute bridges
6. 2x20 monster walks
"""

standardspeedrecovery =  "Hot tub, Peanut Pre practice, Heat pre practice. Protien Drink "

topspeed_recovery = {
    "topspeed1" : standardspeedrecovery,
    "topspeed2" : "",
    "topspeed3" : ""
}
accel_recovery = {
    "accel1" : standardspeedrecovery,
    "accel2" : "",
    "accel3" : ""
}
tempoMF_recovery = {
    "tempoMF1" : "Rolling out, Mobility, Calf Strenghting, Core ",
    "tempoMF2" : "",
    "tempoMF3" : ""
}
tempoW_recovery = {
    "tempoW1" : "Rolling out, Ankle, Mobility, Hips/Hurdles",
    "tempoW2" : "",
    "tempoW3" : ""
}
endurance_recovery = {
    "endurance1" : standardspeedrecovery,
    "endurance2" : "",
    "endurance3" : ""
}
alternatives = {
    "hips": {
        "bad": hips_bad,
        "ok": hips_ok,
        "almost": hips_almost
    },

    "calves": {
        "bad": calves_bad,
        "ok": calves_ok,
        "almost": calves_almost
    },

    "hamstrings": {
        "bad": hamstrings_bad,
        "ok": hamstrings_ok,
        "almost": hamstrings_almost
    },

    "core": {
        "bad": core_bad,
        "ok": core_ok,
        "almost": core_almost
    },

    "quads": {
        "bad": quads_bad,
        "ok": quads_ok,
        "almost": quads_almost
    }
}
almostendurance = """Endurance day soreness — almost
Bike conditioning replacement:

8–10 min easy warmup

10–12 x 30 sec moderate-hard / 60–90 sec easy

8–10 min cooldown

Effort: RPE 6–7
Resistance: low to moderate
Stay seated.

This is the best general replacement for tempo/conditioning without stressing sore tissue."""


#Ok now for the actual coding
def get_schedule_shift():
    if not SHIFT_FILE.exists():
        return 0

    with open(SHIFT_FILE, "r") as file:
        shift_text = file.read().strip()

    if shift_text == "":
        return 0

    return int(shift_text)


def save_schedule_shift(shift_days):
    with open(SHIFT_FILE, "w") as file:
        file.write(str(shift_days))


def shift_schedule_back_one():
    current_shift = get_schedule_shift()
    new_shift = current_shift + 1

    save_schedule_shift(new_shift)

    print(f"Schedule shifted back by 1 day.")
    print(f"Total schedule shift: {new_shift} day(s).")


def reset_schedule_shift():
    save_schedule_shift(0)
    print("Schedule shift reset to 0.")

def subtract_schedule_shift_one():
    current_shift = get_schedule_shift()

    if current_shift <= 0:
        print("Schedule shift is already 0. Nothing to subtract.")
        return

    new_shift = current_shift - 1
    save_schedule_shift(new_shift)

    print("Schedule shift decreased by 1 day.")
    print(f"Total schedule shift is now: {new_shift} day(s).")
########################################### -> Infromation above works schedule shift
def make_sure_log_exists():
    if not LOG_FILE.exists():
        with open(LOG_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["date", "workout", "notes"])


def read_training_log():
    make_sure_log_exists()

    with open(LOG_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    return rows


def write_training_log(rows):
    with open(LOG_FILE, "w", newline="", encoding="utf-8") as file:
        fieldnames = ["date", "workout", "notes"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(rows)


def show_training_log(rows):
    if len(rows) == 0:
        print("Training log is empty.")
        return

    print("\nTraining Log")
    print("-" * 40)

    for index, row in enumerate(rows, start=1):
        print(f"\nEntry #{index}")
        print(f"Date: {row['date']}")
        print(f"Workout: {row['workout']}")
        print(f"Notes: {row['notes']}")


def normalize_date(date_text):
    date_text = date_text.strip()

    # Allows input like 0618
    if len(date_text) == 4 and date_text.isdigit():
        return "2026-" + date_text[:2] + "-" + date_text[2:]

    # Allows input like 2026-06-18
    return date_text


def choose_entry_by_date(rows):
    date_input = input("What date do you want to edit? Use mmdd or yyyy-mm-dd: ")
    chosen_date = normalize_date(date_input)

    matching_entries = []

    for index, row in enumerate(rows, start=1):
        if row["date"] == chosen_date:
            matching_entries.append((index, row))

    if len(matching_entries) == 0:
        print("No entries found for that date.")
        return None

    print(f"\nEntries for {chosen_date}")
    print("-" * 40)

    for index, row in matching_entries:
        print(f"\nEntry #{index}")
        print(f"Workout: {row['workout']}")
        print(f"Notes: {row['notes']}")

    try:
        choice = int(input("Which entry number do you want? "))
    except ValueError:
        print("Invalid entry number.")
        return None

    for index, row in matching_entries:
        if choice == index:
            return choice - 1

    print("That entry number was not listed.")
    return None


def delete_log_entry():
    rows = read_training_log()
    show_training_log(rows)

    entry_index = choose_entry_by_date(rows)

    if entry_index is None:
        return

    removed = rows.pop(entry_index)
    write_training_log(rows)

    print("Entry deleted.")
    print(f"Deleted date: {removed['date']}")


def edit_log_entry():
    rows = read_training_log()
    show_training_log(rows)

    entry_index = choose_entry_by_date(rows)

    if entry_index is None:
        return

    current_entry = rows[entry_index]

    print("\nCurrent entry:")
    print(f"Date: {current_entry['date']}")
    print(f"Workout: {current_entry['workout']}")
    print(f"Notes: {current_entry['notes']}")

    print("\nPress enter to keep the current value.")

    new_date = input("New date: ")
    new_workout = input("New workout: ")
    new_notes = input("New notes: ")

    if new_date.strip() != "":
        current_entry["date"] = normalize_date(new_date)

    if new_workout.strip() != "":
        current_entry["workout"] = new_workout

    if new_notes.strip() != "":
        current_entry["notes"] = new_notes

    rows[entry_index] = current_entry
    write_training_log(rows)

    print("Entry updated.")


def add_manual_log_entry():
    rows = read_training_log()

    date_input = input("Date for new entry, mmdd or yyyy-mm-dd: ")
    date = normalize_date(date_input)

    workout = input("Workout: ")
    notes = input("Notes: ")

    rows.append({
        "date": date,
        "workout": workout,
        "notes": notes
    })

    write_training_log(rows)

    print("Manual entry added.")


def edit_training_log_menu():
    while True:
        print("\nCSV Edit Menu")
        print("-------------")
        print("view   = view the training log")
        print("delete = delete an entry")
        print("edit   = edit an entry")
        print("add    = add a manual entry")
        print("done   = return to main program")

        choice = input("What do you want to do? ").lower().strip()

        if choice == "view":
            rows = read_training_log()
            show_training_log(rows)

        elif choice == "delete":
            delete_log_entry()

        elif choice == "edit":
            edit_log_entry()

        elif choice == "add":
            add_manual_log_entry()

        elif choice == "done":
            break

        else:
            print("Invalid choice. Type view, delete, edit, add, or done.")
########################################### -> Infromation above works the menu.
def get_training_day_info():
    date = input("date in mmdd format (no slashes)") # asks for the date
    trainingdate = datetime.strptime("2026" + date,"%Y%m%d") #turns it into a date
    seasonstart= datetime.strptime("20260601", "%Y%m%d") #turns date into a number
    dayssincestart = (trainingdate - seasonstart).days # if we want to change like we miss a day add 1 day to trianingdate or take one away from season start
    schedule_shift = get_schedule_shift()
    adjusted_dayssincestart = dayssincestart - schedule_shift
    weeknumber = (adjusted_dayssincestart // 7) + 1 # gets the week
    workoutlevel = get_workout_level(weeknumber)
    daynumber = (adjusted_dayssincestart % 7) + 1 #gets the day
    typebynumber = {
        1: "tempoMF",
        2: "accel",
        3: "tempoW",
        4: "endurance",
        5: "tempoMF",
        6: "topspeed",
        7: "rest"
    } # just sets each type of workout into a number to be later used to acess the workout level
    daytype = typebynumber[daynumber]
    return trainingdate, weeknumber, workoutlevel, daytype
def get_workout_level(weeknumber):
        if weeknumber in [1, 2, 3, 5]:
                workoutlevel = "1"
        elif weeknumber in [4,10]:
                workoutlevel = "rest"
        elif weeknumber in [6, 7, 8, 9]:
                workoutlevel = "2"
        elif weeknumber in [11, 12, 13, 14]:
                workoutlevel = "3"
        else:
                workoutlevel = "unknown"
                print("not a valid training week.")
        return workoutlevel
####################t###################### -> Inffromation above works the training date
LOG_FILE = Path(__file__).parent / "training_log.csv" #Path describes the location/name of a file on my computer. By using exists() we can check to see if this file already exists. this also shows its within the same folder
SHIFT_FILE = Path(__file__).parent / "schedule_shift.txt"
def add_to_training_log(trainingdate, workout_text):  # This creates the function
    notes = input("Any additional notes? Press enter if none: ") # setting a variable notes to be used to hold the response

    file_exists = LOG_FILE.exists() # checks to see if the file already exists as said before, through the path that checks the folder

    with open(LOG_FILE, "a", newline="", encoding="utf-8") as file: #the "a" stands for append, for this csv addition, here append means to add to what has already been created. UTF 8 is the rule system for how to store the characters
        writer = csv.writer(file)                                   # the open means that it will open the log file as where it is stored and then now append it. newline creates the proper spacing. named file.
# having the csv.writer access the file that we just previously named which is shown in the line above. Using "with" allows for the file to be closed one we are done.
        if not file_exists: # for the first put of information it makes it so that we have the headers
            writer.writerow(["date", "workout", "notes"])

        writer.writerow([ # this actually writes the workout, this includes the date, the workout, and the notes
            trainingdate.strftime("%Y-%m-%d"),
            workout_text,
            notes
        ])
# we only want to call this fucntion after we are given the workut for the day

    print("Workout added to training_log.csv")
answer1 = input("workout, recovery, info, edit, shift?") #asks the first question
#below works to get the proper exercises

if answer1 == "workout":
    trainingdate, weeknumber, workoutlevel, daytype = get_training_day_info()
    if workoutlevel == "rest" or daytype == "rest":
        print("Rest day.")

    else:
        session = daytype + workoutlevel
        liftsession = daytype + "lift" + workoutlevel
        if daytype == "accel":
            plannedworkout = ("Running:\n" + accel[session] + "\n\n" + "Lifting:\n" + accellift[liftsession]) # uses the created variable session to go within the accel dictionary and bring out the proper information, same with the liftsession

        elif daytype == "topspeed":
            plannedworkout = ("Running:\n"+ topspeed[session] + "\n\n" + "Lifting:\n" + topspeedlift[liftsession])

        elif daytype == "tempoMF":
            plannedworkout = (tempoMF[session])

        elif daytype == "tempoW":
            plannedworkout = (tempoW[session])

        elif daytype == "endurance":
            endurance_running = endurance_by_week.get(
                weeknumber,
            "No endurance workout has been entered")

            plannedworkout = ("Running:\n" + endurance_running + "\n\nLifting:\n" + endurancelift[liftsession])
        soreness = input("soreness? hips/calves/hamstrings/core/quads/none") # asks the question about the soreness
        if soreness == "none":
            print("Planned workout:")
            print(plannedworkout)
            adder = input("Do you want to add this workout to the log? yes/no: ")
            if adder == "yes":
                add_to_training_log(trainingdate, plannedworkout)
        elif soreness not in alternatives:
            print("invalid")
        else:
            level = input("How bad? rest/bad/ok/almost: ") # based on level chooses the correct output
            if level not in ["bad", "ok", "almost", "rest"]:
                print("Invalid level. Type bad, ok, or almost.")
            elif level == "rest":
                print("rest day")
                adder = input("Do you want to add this workout to the log? yes/no: ") # this asks the question for when soreness is not equal to none, after we have already determined the workout
                if adder == "yes":
                    add_to_training_log(trainingdate, "rest day")
            elif daytype == "endurance" and level == "almost":
                modifiedworkout = almostendurance
                print("Modified workout:")
                print(almostendurance)
                adder = input("Do you want to add this workout to the log? yes/no: ") # this asks the question for when soreness is not equal to none, after we have already determined the workout
                if adder == "yes":
                    add_to_training_log(trainingdate, modifiedworkout)
            elif daytype in ["tempoMF", "tempoW"] and level in ["almost","ok"]:
                modifiedworkout = "6xwalk,skip,jogs"
                print(modifiedworkout)
                adder = input("Do you want to add this workout to the log? yes/no: ") # this asks the question for when soreness is not equal to none, after we have already determined the workout
                if adder == "yes":
                    add_to_training_log(trainingdate, modifiedworkout)
            elif daytype in ["tempoMF","tempoW"] and level == "bad":
                modifiedworkout = "15 min bike and mobility/any strengthening"
                print(modifiedworkout)
                adder = input("Do you want to add this workout to the log? yes/no: ") # this asks the question for when soreness is not equal to none, after we have already determined the workout
                if adder == "yes":
                    add_to_training_log(trainingdate, modifiedworkout)
            else:
                modifiedworkout = alternatives[soreness][level]
                print("Modified workout:")
                print(modifiedworkout)
                adder = input("Do you want to add this workout to the log? yes/no: ") # this asks the question for when soreness is not equal to none, after we have already determined the workout
                if adder == "yes":
                    add_to_training_log(trainingdate, modifiedworkout)
elif answer1 == "recovery": # gives the reccovery based on the daytype
    trainingdate, weeknumber, workoutlevel, daytype = get_training_day_info()
    session = daytype + workoutlevel
    if daytype == "accel":
        plannedworkout = (accel_recovery[session])

    elif daytype == "topspeed":
        plannedworkout = (topspeed_recovery[session])

    elif daytype == "tempoMF":
        plannedworkout = (tempoMF_recovery[session])

    elif daytype == "tempoW":
        plannedworkout = (tempoW_recovery[session])

    elif daytype == "endurance":
        plannedworkout = (endurance_recovery[session])
    print(plannedworkout)
elif answer1 == "info": # gives the general information about info
    info1 = input("raining,core,mobility,foot,hipshurdles, subtractshift, resetshift")
    if info1 == "raining":
        trainingdate, weeknumber, workoutlevel, daytype = get_training_day_info()
        if workoutlevel == "rest" or daytype == "rest":
            print("Rest day.")
        else:
            if daytype == "accel":
                print(indoor_accel_topspeed)
            elif daytype == "topspeed":
                print(indoor_accel_topspeed)
            elif daytype == "tempoMF":
                print("15 min bike and mobility/any strengthening")
            elif daytype == "tempoW":
                print("15 min bike and mobility/any strengthening")
            elif daytype == "endurance":
                print(indoor_endurance)
            else:
                print("invalid")
    elif info1 == "core":
        print(core)
    elif info1 == "mobility":
        print(mobility)
    elif info1 == "foot":
        print(foot_strength)
    elif info1 == "hipshurdles":
        print(hipshurdles)
    elif info1 == "resetshift":
        reset_schedule_shift()
    elif info1 == "subtractshift":
        subtract_schedule_shift_one()
    else:
        print("invalid")
elif answer1 == "edit":
    edit_training_log_menu() # calls the training log menu
elif answer1 == "shift":
    shift_schedule_back_one()
else:
    print("Invalid answer. Type workout or recovery.")
