holidays = int(input())

working_days = 365 - holidays

working_days_playtime_in_min = working_days * 63
holidays_playtime_in_min = holidays * 127
total_playtime_in_min = working_days_playtime_in_min + holidays_playtime_in_min

diff = abs(total_playtime_in_min-30000)
hours_for_play_diff = diff // 60
minutes_for_play_diff = diff % 60

if total_playtime_in_min >= 30000:
    print("Tom will run away")
    print(f"{hours_for_play_diff} hours and {minutes_for_play_diff} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hours_for_play_diff} hours and {minutes_for_play_diff} minutes less for play")