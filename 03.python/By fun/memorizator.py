import random
korean = ["긴장을 풀다", "감사하는","불평하다","기쁜","급행의","보상","좌절한","인식하다","성질","사찰",
          "물체","실망한","불안한","고집하다","갑작스러운","즉각적인","직접의","감사하다","창백한","목적",
          "경주","낙담한","응시하다","파열","비참한","당황한","거의~하지 않다","당황하다","일치하다","잔인한",
          "결정적인","고립된","어색한","연민","무시무시한","낙관적인","성실한","가능성이 있는","견디다","반사하다",
          "비슷한","상황","관련이 있는","가정하다","사회적인","독특한","선호하다","유지하다","흐트러뜨리다","지역",
          "사과하다","나타내다","동료","의지하다","실수","요청","생각하다","거절하다","답장","등급",
          "능력","열정","둘러싸다","정말","모방하다","끈","얻다","소중한","기여하다","나눠주다",
          "거절하다","시선","아끼다","환대","폭로하다","무심한","서로의","송별 인사","빚자다","치료하다",
          "주석","대중적인","개발하다","순간","대중","약속하다","선택하다","즐거움","포함하다","진화하다",
          "범위","물건","물질","잡지","묘사하다","서술하다","그 외에는","공유하다","질투하는","번역하다",
          "고개를 끄덕이다","의미하다","결론을 내리다","의도하다","가치","결과","영광","내적인","언어의","게다가",
          "치료하다","중심부","치다","경로","감사","은유","해석하다","모욕하다","이상한","무작위의","발언","문장"]
english = ["relax","grateful","complain","joyful","express","reward","frustrated","perceive","temper","monastery","object","disappointed","anxious","stubborn","sudden","instant","direct","appreciate","palete","purpose","race","discouraged","gaze","rupture","miserable","embarrassed","barely","flustered","match","cruel","decisive","isolated","awkward","compassion","terrifying","optimistic","faithful","potential","endure","reflect","similar","situation","relevant","assume","social","unique","prefer","maintain","disrupt","region","apologize","demonstrate","colleague","rely","mistake","request","consider","refuse","reply","grade","ability","passion","surround","indeed","imitate","string","obtain","precious","contribute","distribute","decline","glance","cherish","hospitality","expose","indifferent","mutual","farewell","lendable","treat","annotation","popular","unveil","instantaneous","audience","promise","select","pleasure","include","evolve","range","item","substance","magazine","depict","narrate","otherwise","share","jealousy","translate","nod","mean","conclude","intend","value","outcome","glory","intrinsic","linguistic","moreover","therapy","core","strike","route","gratitude","metaphor","interpret","insult","peculiar","random","remark","sentence"]
korean1 = ["긴장을 풀다", "감사하는","불평하다","기쁜","급행의","보상","좌절한","인식하다","성질","사찰","물체","실망한","불안한","고집하다","갑작스러운","즉각적인","직접의","감사하다","창백한","목적","경주","낙담한","응시하다","파열","비참한","당황한","거의~하지 않다","당황하다","일치하다","잔인한","결정적인","고립된","어색한","연민","무시무시한","낙관적인","성실한","가능성이 있는","견디다","반사하다","비슷한","상황","관련이 있는","가정하다","사회적인","독특한","선호하다","유지하다","흐트러뜨리다","지역","사과하다","나타내다","동료","의지하다","실수","요청","생각하다","거절하다","답장","등급","능력","열정","둘러싸다","정말","모방하다","끈","얻다","소중한","기여하다","나눠주다","거절하다","시선","아끼다","환대","폭로하다","무심한","서로의","송별 인사","빚자다","치료하다","주석","대중적인","개밣하다","순간","대중","약속하다","선택하다","즐거움","포함하다","진화하다","범위","물건","물질","잡지","묘사하다","서술하다","그 외에는","공유하다","질투하는","번역하다","고개를 끄덕이다","의미하다","결론을 내리다","의도하다","가치","결과","영광","내적인","언어의","게다가","치료하다","중심부","치다","경로","감사","은유","해석하다","모욕하다","이상한","무작위의","발언","문장"]
english1 = ["relax","grateful","complain","joyful","express","reward","frustrated","perceive","temper","monastery","object","disappointed","anxious","stubborn","sudden","instant","direct","appreciate","palete","purpose","race","discouraged","gaze","rupture","miserable","embarrassed","barely","flustered","match","cruel","decisive","isolated","awkward","compassion","terrifying","optimistic","faithful","potential","endure","reflect","similar","situation","relevant","assume","social","unique","prefer","maintain","disrupt","region","apologize","demonstrate","colleague","rely","mistake","request","consider","refuse","reply","grade","ability","passion","surround","indeed","imitate","string","obtain","precious","contribute","distribute","decline","glance","cherish","hospitality","expose","indifferent","mutual","farewell","lendable","treat","annotation","popular","unveil","instantaneous","audience","promise","select","pleasure","include","evolve","range","item","substance","magazine","depict","narrate","otherwise","share","jealousy","translate","nod","mean","conclude","intend","value","outcome","glory","intrinsic","linguistic","moreover","therapy","core","strike","route","gratitude","metaphor","interpret","insult","peculiar","random","remark","sentence"]

print("Welcome to the English-Korean memorizer!")
print("we'll start en to kr quiz first.")
for _ in range(len(korean)):
    idx = random.randint(0, len(korean)-1)
    print(f"{korean[idx]:}")
    ans = input()
    if ans == english[idx]:
        print("Correct!")
    else:
        print(f"Wrong! The answer is {english[idx]}")
    korean.pop(idx)
    english.pop(idx)
    
print("Now, we'll start kr to en quiz.")
for _ in range(len(korean1)):
    idx = random.randint(0, len(korean1)-1)
    print(f"{english1[idx]:}")
    ans = input()
    if ans == korean1[idx]:
        print("Correct!")
    else:
        print(f"Wrong! The answer is {korean1[idx]}")
    korean1.pop(idx)
    english1.pop(idx)