from sys import exit
from sys import stdout
import time
import random 
from textwrap import dedent
from copy import deepcopy

print("由于游戏中存在大量文字，因此在游戏开始前，请告诉我你希望文字出现的速度。）")
print("你可以选择1.慢（故事模式）2.快（闯关模式）3.瞬间出现（调试模式）")
choose = input("请输入数字--->")
if choose == '1':
    def print_time(text):
        stdout.write(" \r"+ "\r\n") # /r 光标回到行首
        stdout.flush() #把缓冲区全部输出
        for c in text:
            stdout.write(c)
            stdout.flush()
            time.sleep(0.1)
elif choose == '2':
    def print_time(text):
        stdout.write(" \r"+ "\r\n") # /r 光标回到行首
        stdout.flush() #把缓冲区全部输出
        for c in text:
            stdout.write(c)
            stdout.flush()
            time.sleep(0.05)
elif choose == '3':
    def print_time(text):
        print(text)
else:
    print('你没有选择数字，系统默认为故事模式')
    def print_time(text):
        stdout.write(" \r"+ "\r\n") # /r 光标回到行首
        stdout.flush() #把缓冲区全部输出
        for c in text:
            stdout.write(c)
            stdout.flush()
            time.sleep(0.1)


adr=[0,0]
YOU={}#先声明变量


class Scene(object):

    def enter(self):
        print_time("This scene is not yet configured")
        print_time("Subclass it and implement enter().")
        exit(1)
#战后奖励
def battle_reward(you):
    i=random.randrange(30) 
    print_time("现在，你可以自由挑选你的战斗奖励：")
    print_time("1.你的剑术修为更上一层楼。\n")
    print_time("2.你对格挡能力有了更深的理解。\n")
    print_time("3.你领悟了新的战斗步伐。\n")
    print_time("4.在战斗中，你觉醒了更多的先祖血脉。\n")
    choose=input("请选择数字！--->")
    if choose=='1':
        you['攻击']+=1
        print_time("攻击+1")
        if you['悟性']>=i:
            you['攻击']+=1
            print_time("你的高悟性令你的战斗力得到了进一步提升，攻击+1")
    elif choose=='2':
        you['护甲']+=1
        print_time("护甲+1")
        if you['悟性']>=i:
            you['护甲']+=1
            print_time("你的高悟性令你的战斗力得到了进一步提升，护甲+1")
    elif choose=='3':
        you['速度']+=1
        print_time("速度+1")
        if you['悟性']>=i:
            you['速度']+=1
            print_time("你的高悟性令你的战斗力得到了进一步提升，速度+1")
    elif choose=='4':
        you['生命上限']+=1
        print_time("生命上限+1")
        if you['悟性']>=i:
            you['生命上限']+=1
            print_time("你的高悟性令你的战斗力得到了进一步提升，生命上限+1")
    else:
        print_time("你没有选择应有的选项，机会稍纵即逝，你的迟疑令你失去了宝贵的战斗奖励")
    show_atr(you)


#死亡结局
def dead(why):
    global you
    global loc
    print_time(why)
    print_time("你本次死亡时的人物属性如下所示。\n")
    show_atr(you)
    print_time("死亡并非终点，而是又一次选择")
    print_time("请问选择1.退出游戏还是 2.吃下后悔药？")
    choose = input("请选择数字--->")
    if choose == '1':
        print_time("希望你享受到了片刻愉悦，再见。\n")
        exit(0)
    elif choose == '2':
        loc=deepcopy(adr)
        you=deepcopy(YOU)
        print_time("你吃下了后悔药，你回到了上一次遇见生命之泉的时候。\n")
        show_atr(you)
    else:
        print_time("机不可失，后悔药飞走了。\n")
        exit(0)


#model={'血量':,'攻击':,'护甲':,'速度':,'生命上限':,'悟性':,'吸血':}
#战斗
def battle(you,enemy):
    print_time("战斗开始！")
    if you['攻击']<=enemy['护甲']:
        dead("未能击穿敌方护甲，你战败了")
    elif you['护甲']>=enemy['攻击']:
        print_time ("战斗结束，意料之内的胜利！")
        battle_reward(you)
    else:
        if you['速度']>=enemy['速度']:
            yourturn=True
        else:
            yourturn=False
        while (you['血量']>0) and (enemy['血量']>0):
            if yourturn == True:
                enemy['血量']=enemy['血量']-(you['攻击']-enemy['护甲'])
                print(f"你对敌人造成了{(you['攻击']-enemy['护甲'])}点伤害。\n")
                if '吸血' in you:
                    you['血量']+=(you['攻击']-enemy['护甲'])*you['吸血']
                    if you['血量']>you['生命上限']:
                        print(f"你的吸血效果使你回复了{((you['攻击']-enemy['护甲'])*you['吸血'])-(you['生命上限']-you['血量'])}点生命")
                        you['血量']=you['生命上限']
                    else:
                        print(f"你的吸血效果使你回复了{(you['攻击']-enemy['护甲'])*you['吸血']}点生命")
                print_time(f"你还有{you['血量']}点血量。\n")
                yourturn = False
            else:
                you['血量']=you['血量']-(enemy['攻击']-you['护甲'])
                print(f"敌人对你造成了{(enemy['攻击']-you['护甲'])}点伤害。\n")
                if '吸血' in enemy:
                    enemy['血量']+=(enemy['攻击']-you['护甲'])*enemy['吸血']
                    if enemy['血量']>enemy['生命上限']:
                        print(f"你的吸血效果使你回复了{((enemy['攻击']-you['护甲'])*enemy['吸血'])-(enemy['生命上限']-enemy['血量'])}点生命")
                        enemy['血量']=enemy['生命上限']
                    else:
                        print(f"敌人的吸血天赋使其回复了{(enemy['攻击']-you['护甲'])*enemy['吸血']}点生命")
                print_time(f"敌人还有{enemy['血量']}点血量。\n")
                yourturn = True
        if you['血量']<=0:
            dead("难以置信，你战败了")
        else:
            print_time ("战斗结束，意料之内的胜利！")
            battle_reward(you)
#遭遇敌人后选择
def meet(enemy):
    print("你的选择是：\n1.我的剑渴求着敌人的鲜血。\n2.感觉打不过，溜了溜了。\n")
    choose=input("请输入数字--->")
    if choose=='1':
        battle(you,enemy)
    elif choose=='2':
        if you['速度']>=enemy['速度']:
            print_time('你成功逃脱了怪物的追击')
        else:
            print_time("你没能逃脱，无奈只能进行战斗")
            battle(you,enemy)
    else:
        print("请输入数字！")
        return meet(enemy)
#展示人物模板
def show_atr(you):
    print(f"你的英雄模板为：\n血量：{you['血量']}\n攻击：{you['攻击']}\n护甲：{you['护甲']}\n速度：{you['速度']}\n生命上限：{you['生命上限']}\n悟性：{you['悟性']}\n装备：{you['装备']}\n称号：{you['称号']}")
    if '吸血' in you:
        print_time(f"吸血：{you['吸血']}")


#游戏开始
print_time("来自未知纪元、未知世界的勇士，请举起你手中的无名之剑，书写属于你自己的英雄史诗。\n")

name=input("请输入你的名字--->")
print_time(f"{name}，这真是一个好名字！")

print_time(f"{name}，现在请你回答一个问题，这将直接影响你的英雄模板属性。\n")
print_time("你希望自己是什么样的英雄呢？")
print_time("1.英勇的战士，手持重剑，陷阵于千军万马而不死。\n")
print_time("2.冷血的剑手，剑法轻灵，五步之内，夺人肝胆，取人性命。\n")
print_time("3.沉默的杀手，身法似鬼魅，短剑如毒蛇，匿于暗处，伺机待发。\n")
print_time("4.天生的剑神，注定站在剑道绝巅的人，只是如今还很弱小。\n")
choose=input("请输入数字--->")
if choose == '1':
    you={'血量':50,'攻击':5,'护甲':10,'速度':5,'生命上限':50,'悟性':4,'装备':[],'称号':[],'状态':[]}
elif choose == '2':
    you={'血量':35,'攻击':8,'护甲':6,'速度':7,'生命上限':35,'悟性':7,'装备':[],'称号':[],'状态':[]}
elif choose == '3':
    you={'血量':25,'攻击':10,'护甲':4,'速度':10,'生命上限':25,'悟性':9,'装备':[],'称号':[],'状态':[]}
elif choose == '4':
    you={'血量':20,'攻击':5,'护甲':4,'速度':4,'生命上限':20,'悟性': 16,'装备':[],'称号':[],'状态':[]}
else:
    print_time("你没有选择英雄模板，你只是一个平平无奇的普通人，却因你的无知进入了这个危机四伏的世界。\n")
    you={'血量':20,'攻击':5,'护甲':5,'速度':4,'生命上限':20,'悟性': 5,'装备':[],'称号':[],'状态':[]}


show_atr(you)
print_time("现在，黑暗降临了......\n\n\n")

#荒原篇尾声
class WildernessEnd(Scene):
    def enter(self):

        print_time("本游戏的荒原篇结束了，这一篇章花费了作者三天的时间去构思和学习，但如果作为本人的制作的第一个游戏，它如果可以为玩家带去快乐的话，那么便足慰我心了。最后来看看在荒原篇结尾，你的人物已经被你玩成什么样了：")
        show_atr(you)
        return '荒原篇尾声'


#剩余场景写在别的文件,导入到这个地方

#序章
class Prologue(Scene):
    def enter(self):
        global you
        global loc
        global adr
        global YOU
        bat={'血量':10,'攻击':5,'护甲':1,'速度':5,'生命上限':10}
        print_time(f'''"{name},{name}!醒醒！快醒醒！它们要来了!"''')
        print_time(f"....是谁在叫我....")
        print_time("你终于睁开双眼，却看到了一个满目疮痍的世界。\n")
        print_time("遍布残骸的荒凉中，有面目狰狞的怪物游荡着，从它们脚下的废墟中，依稀还能看出些许人类文明的灰烬。\n")
        print_time("你挣扎着起身，想找到那个在黑暗中唤醒你的声音，四下环顾，却一无所获。\n")
        print_time("你的举动引起了一只暴躁的蝙蝠的注意，它从一具不知是人是兽的躯壳中人立而起，向你迎面飞来。\n")
        print_time("你还没搞清楚现在的状况，但是眼下却容不得你思考或是回忆。\n")
        print_time("千钧一发间，你的选择是：\n1.握紧手中的无名长剑，开始你的异界第一战。\n2.状况未明，不如先逃到安全的地方。\n")
        choose=input("请输入数字--->")
        if choose=='1':
                battle(you,bat)
                print_time("由于你即刻进行了一场战斗，那残留在你身体中还未消散的、将你从原本世界带到异界的神秘力量在战斗中得以发酵。\n")
                print_time("你的全属性+1")
                you['血量']+=1
                you['攻击']+=1
                you['护甲']+=1
                you['速度']+=1
                you['生命上限']+=1
                you['悟性']+=1
                show_atr(you)
        elif choose=='2':
            if you['速度']>=bat['速度']:
                print_time('你成功逃脱了怪物的追击')
                print_time(f'''你一路奔逃，突然有一个声音叫住了你。"{name},你的选择真是有趣。"''')
                print_time("你转身，看见一个难以名状的生物正在叫你的名字。你不知道怎么去形容它，但是却并不觉得恐惧。\n")
                print_time('''“你是谁？”你这样问道，“这里又是哪里？”\n那个存在低笑着回答道：“这里是神明遗忘的地方，而我只是一个无聊的存在。”''')
                print_time('''“但现在我发现了一个有趣的家伙，”它的声调变得高了些，“一个谨慎的勇士，或者说一个胆怯的英雄，\n你的到来可能会使这里变得更有意思。”''')
                print_time('''“不过，这里对现在的你来说还是太过危险了，为了让你继续有趣下去，也许我应该送你一个小礼物。”''')
                print_time("不知何时它已经消失了，而你蓦然发现，自己的鞋边上竟缠绕着一圈晦涩的、散发幽幽蓝光的咒文，你感到自己变得更加轻盈了。\n")
                print_time("由于你逃避了来到这个世界的第一次战斗，你引起了未知存在的兴趣并获得了馈赠，你得到了史诗级靴子【自由】，你的速度+10，悟性+2")
                you['速度']+=10
                you['悟性']+=2
                you['装备'].append('【史诗级靴子】“自由”')
                show_atr(you)
            else:
                print_time("你没能逃脱，无奈只能进行战斗")
                battle(you,bat)
                print_time("这是你的第一次战斗，那残留在你身体中、还未消散的、将你从原本世界带到异界的神秘力量在战斗中得以发酵。\n")
                print_time("你的全属性+1")
                you['血量']+=1
                you['攻击']+=1
                you['护甲']+=1
                you['速度']+=1
                you['生命上限']+=1
                you['悟性']+=1
                show_atr(you)
                print_time(f'''正当你沉浸于力量的提升时，突然有一个声音叫住了你。"{name},你的选择真是有趣。"''')
                print_time("你转身，看见一个难以名状的生物正在叫你的名字。你不知道怎么去形容它，但是却并不觉得恐惧。\n")
                print_time('''“你是谁？”你这样问道，“这里又是哪里？”\n那个存在低笑着回答道：“这里是神明遗忘的地方，而我只是一个无聊的存在。”''')
                print_time('''“但现在我发现了一个有趣的家伙，”它的声调变得高了些，“一个谨慎的勇士，或者说一个胆怯的英雄，\n你的到来可能会使这里变得更有意思。”''')
                print_time('''“不过，这里对现在的你来说还是太过危险了，为了让你继续有趣下去，也许我应该送你一个小礼物。”''')
                print_time("不知何时它已经消失了，而你蓦然发现，自己的鞋边上竟缠绕着一圈晦涩的、散发幽幽蓝光的咒文，你感到自己变得更加轻盈了。\n")
                print_time("由于你选择逃避来到这个世界的第一次战斗，你引起了未知存在的兴趣并获得了馈赠，你得到了史诗级靴子【自由】，你的速度+10，悟性+2")
                you['速度']+=10
                you['悟性']+=2
                you['装备'].append('【史诗级靴子】“自由”')
                show_atr(you)
        else:
            print_time("你没有输入正确的数字，你的迟疑使你被蝙蝠偷袭成功。\n")
            print_time("你被蝙蝠击倒了。\n")
            print_time('''出师未捷身先死，长使英雄泪满襟。还请重新来过，下次记得老老实实选择选项哦。\n''')
            exit(0)

        print_time("你还是不知道自己该何去何从，但是你知道，你必须离开这个怪物横行的荒原。\n\n\n")
        YOU=deepcopy(you)
        return "荒原"
        
#荒原 
class Wilderness(Scene):
    #荒原事件字典
    def __init__(self):
        self.eventdic={(-13,14):self.event01,(0,-17):self.event02,(-9,11):self.event03,(12,9):self.event04,(0,5):self.event05,
        (3,4):self.event06,(3,8):self.event07,(13,13):self.event08}
    #[-1,13]:event06(),[-17,-10]:event07(),[13,7]:event08(),[16,1]:event09(),[-19,18]:event10(),[12,-19]:event11(),
    #[15,-19]:event12(),[5,0]:event13(),[-9,-1]:event14(),[17,-5]:event15(),

    #荒原事件函数
    #沉默之虎事件
    def event01(self):
        tiger={'血量':100,'攻击':100,'护甲':20,'速度':20,'生命上限':100}
        print_time("......\n你突然觉得如芒在背，似乎有什么可怕的东西正在注视着自己。\n")
        print_time("当你发现那道目光的主人时，已经有些太迟了，一束黑影从极远处向你电驰而来，迎面能嗅到浓郁的腥气。\n")
        print_time("你甚至没能完全看清这只怪物的样貌，但它的身形像极了原世界中的老虎。\n")
        print_time("你侵犯了沉默之虎的领地，你将面对这只荒野顶级掠食者的追杀，不死不休。\n")
        print_time('''"只能迎战了！"''')
        battle(you,tiger)
        print_time("沉默之虎是站在荒野食物链顶端的存在，令人惊叹的是你击杀了它！")
        print_time("你获得【史诗】称号【掠食者之灾】")
        print_time("称号加成：攻击+5，护甲+5，速度+5")
        you['攻击']+=5
        you['护甲']+=5
        you['速度']+=5
        you['称号'].append('【史诗级称号】“掠食者之灾”')
        show_atr(you)
    
    #无头骑士事件
    def event02(self):
        death_knight={'血量':150,'攻击':70,'护甲':70,'速度':30,'生命上限':150}
        print_time('''......\n"迷途的旅者，向吾证明你的力量。"''')
        print_time("还在旷野中寻找出路的你兀然听到一个厚重的、威严的声音。\n")
        print_time("你循声而看，只见一个被铁甲覆盖全身的无头骑士出现在你的视线边界。\n")
        print_time("他手持一柄漆黑长枪，身体面对着你，没有头颅却能够发出声音。\n")
        print_time("他胯下是一匹神骏却暴躁的黑马，四蹄边缘都燃烧着幽蓝色火焰，双眼赤红，偶尔打个响鼻。\n")
        print_time('''"吾乃生者的恐惧，迷途者的希望，向吾证明你的力量，生之门就会为你而开。"''')
        print_time("是否向无头骑士发起挑战？（注：这是你唯一一次挑战死灵骑士的机会，但也要量力而行。）")
        choose=input("是/否")
        if choose == '是':
            battle(you,death_knight)
            print_time('''“你证明了你的力量，迷途者，感谢你让我解脱，”在消散前，无头骑士说道，“你离生门，还差三步......”''')
            print_time("你击败了荒野边界的死灵骑士，你获得【史诗】称号【迷途者】")
            print_time("称号加成：护甲+5，生命上限+20")
            you['护甲']+=5
            you['生命上限']+=20
            you['称号'].append('【史诗级称号】“迷途者”')
            show_atr(you)
        elif choose == '否':
            print_time('''“旅人，你的胆怯让我不屑。”那骑士如是说道，踏着梦魇马缓缓离去。\n''')
            print_time("远处传来黑马的响鼻声，似乎连梦魇都在嘲弄着你的胆怯。\n")
        else:
            print_time("你的犹豫让你失去了挑战无头骑士的机会。\n")

    #荒原求生者事件
    def event03(self):
        leopard={'血量':60,'攻击':60,'护甲':20,'速度':40,'生命上限':60}
        print_time ("......\n你听见了杂乱的声响。\n")
        print_time("!!你看见了一个探险家模样的男人！他正在躲避一只斑豹的追赶。\n")
        print_time("那只斑豹的速度太快了，眼看男人就要被追上，这时他看见了你。\n")
        print_time('''“嘿伙计！救救我！看在上帝的份上，我愿意把我身上所有的东西都给你！”''')
        print_time("你可以：1. 拔剑相助。2.漠不关心地离去。\n")
        choose = input("请输入数字--->！")
        if choose == '1':
            battle(you,leopard)
            print_time("你救下了那个男人，但你也因此受了不轻的伤")
            print_time('''“谢谢你勇士！我该怎么感谢你呢？”男子一边说着一边向你走过来。\n''')
            print_time("说话间他突然掏出了一柄泛着幽光的匕首，狠狠地刺向你的脖颈。\n")
            print_time("你下意识地用手肘格挡了匕首，并反身一剑刺穿了男子的喉咙。\n")
            print_time('''“为什么？！”你怒声质问他。\n''')
            print_time("男子捂着喉咙，大口咳血，最终一言不发地死去了。\n")
            print_time("你感染了剧毒，你的血量减半。\n")
            print_time("出门在外要警惕陌生人，你悟了，悟性+2")
            you['血量']*=0.5
            you['悟性']+=2
            show_atr(you)
        
        elif choose == '2':
            print_time("你目睹那个男人惨死在斑豹口下，他绝望并怨毒地看着你离去的背影，并在临死前诅咒你")
            print_time("你受到了一个普通人的死前诅咒，生命上限-3")
            you['状态'].append('“探险者的诅咒”')
            you['生命上限']-=3
            print_time("冷漠不是冷血，对生命要有应有的敬畏。你悟了，悟性+1")
            you['悟性']+=1
            show_atr(you)
        
        else:
            print_time('请输入数字!')
            return self.event03()

    #荒野魔女事件
    def event04(self):
        print_time("......\n长时间的跋涉令你有些走神,你决定坐地小憩片刻。\n")
        print_time("你的双目游离在了野地里的一棵野草上。\n")
        print_time("荒野午间的风正烈，那颗草却依旧倔强地随风摇摆，一只白玉般的赤足踩到那株草上，惹得你双眼往上一搭。\n")
        print_time("那女孩样貌精致，眼角的黑痣略显媚意，眼神却纯净如深湖，她赤足白裙，在这潦草狼藉的荒野中显得十分刺眼。\n")
        print_time("女孩静静的看着你，虽然一言不发，但是那双明媚的双眼似乎已经对你诉说了千回百转。\n")
        print_time("这时候你已经看呆了，而女孩也终于开口。\n")
        print_time('''“我好看吗？”''')
        print_time("你可以选择：")
        print_time("1.回答好看。\n")
        print_time("2.口是心非，回答不好看。\n")
        print_time("3.沉默着对她发起进攻。\n")
        print_time("4.事有蹊跷，转身就跑。\n")
        choose=input("请输入数字--->")
        if choose == '1':
            print_time("女孩捂嘴轻笑，刹那间的风情让你陷入失神状态。\n")
            print_time("等你回过神时，周遭只余你一人，你发现自己嘴角干涸，形容枯槁，身上尘土甚多，时间似乎已经过去了不止一日。\n")
            print_time("你遭遇了魔女，并被其魅惑了两天，被其当成工具人在荒野中猎杀了许多怪物。（没有战斗奖励）")
            print_time("你的血量减半")
            you['血量']*=0.5
            show_atr(you)

        elif choose == '2':
            print_time("你惹恼了荒野魔女，她对你施加了魔女一族的诅咒。\n")
            print_time("你的护甲永久-3")
            you['护甲']-=3
            you['状态'].append('魔女的诅咒')
            show_atr(you)

        elif choose == '3':
            print_time("魔女族最怕的就是不讲道理的男人，你的蛮横攻击让魔女无计可施。\n")
            print_time("她求饶了，为此她可以付出代价。\n")
            print_time("你在荒原以天为被，以地为床，与魔女度过了一夜欢愉，第二天一早神清气爽地出发了。\n")
            print_time("你取悦了魔女，获得了魔女一族的祝福，护甲+3")
            you['护甲']+=3
            you['状态'].append('魔女的祝福')
            show_atr(you)
        elif choose == '4':
            print_time("你的机警让你与荒野上最美的雌性失之交臂。\n")
            print_time("你获得【暗金级称号】“机灵的直男”")
            print_time("护甲+5")
            you['护甲']+=5
            you['称号'].append('【暗金级称号】“机灵的直男”')
            show_atr(you)
        else :
            print_time("你的犹豫让你失去了接触荒野最美雌性的机会。\n")

    #剑冢事件
    def event05(self):
        print_time("......\n你感到了一种冥冥中的呼唤。\n")
        print_time("你闭上双眼跟随心声，来到了一处洞窟。\n")
        choose = input("是否进入？ 是/否")
        if choose == '否':
            print_time("你不敢冒险，带着些许遗憾离开了这个洞窟，往后终其一生，你都没能再次回到这里一探究竟。\n")
        elif choose == '是':
            print_time("你小心地、慢慢地走入洞窟，这洞窟初极狭，才通人，复行数十步，豁然开朗。\n")
            print_time("突如其来的光明让你的双目一时难以适应，等你慢慢睁开双眼，你发现这洞窟内部竟然亮如白昼。\n")
            print_time("千万柄长短不一，形状各异的剑器散插在地，各自散发着淡淡的白色荧光。\n")
            print_time("最明亮的还是中央一柄半人粗细的八面汉剑，剑刃粼光四射，血槽晦暗，气度森严，剑身上还刻有字句")
            print_time("你走近观察，发现上书‘气生万景环成屈龙’八个大字，字锋处险象环生，甚至有些难以直视。\n")
            print_time("一道温润的声音在你心头响起，“来者是客，学一道剑法再走。”")
            print_time("这声音如暖玉温吞，让人不自觉放松，浑然不像是一个剑客。你迟疑地问道:“你是谁？”")
            print_time("“与你一样，剑道行路人尔。”那声音轻笑，随后问道，“告诉我，你觉得剑道最重要的一字是什么？”")
            print_time("你有多种回答选择：")
            print_time("1.斩，2.心，3.御，4.我不知道")
            choose = input("请回答数字！")
            if choose == '1':
                print_time('''“斩，是为剑道第一课，你以此为剑道之基，可见心性坚定。既如此，我便授你一式拔剑术，早年间我曾赖此术纵横江野，
    未尝一败。”那洞窟主人如此说道，之后便不再言语。而你在这片沉默中，突然觉得眉心一疼，脑海中涌入了一道道莫可言喻的信息。''')
                print_time("你学会了【史诗剑法】“斩天拔剑术”,攻击+10，速度+10")
                you['状态'].append('【史诗剑法】“斩天拔剑术”')
                you['攻击']+=10
                you['速度']+=10
            elif choose == '2':
                print_time('''“剑心通明，方可入上境，看来你已触到了剑道真谛。既如此，我便授你一道剑诀，此诀是我中年时拜访宗师名派，融汇百家剑诀而成，
    可助人攀上剑道更高峰，所谓剑心通明，不外如是。”那洞窟主人如此说道，之后便不再言语。而你在这片沉默中，突然觉得眉心一疼，脑海中涌入了一道道莫可言喻的信息。''')
                print_time("你学会了【史诗剑法】“剑心诀”,攻击+7，悟性+4")
                you['状态'].append('【史诗剑法】“剑心诀”')
                you['攻击']+=7
                you['悟性']+=4
            elif choose == '3':
                print_time('''“御者，可御敌，可御剑，攻守兼备，实为兵道也。看来你虽有剑气剑意，却并未行在剑道之上，既如此，我便授你一篇左道。此道乃我平生一大敌所创，
    此人虽败于我手，却可称为豪雄，我虽杀他，却也敬他，此法门似剑非剑，却是旁门左道之集大成者。”那洞窟主人如此说道，之后便不再言语。而你在这片沉默中，突然觉得眉心一疼，脑海中涌入了一道道莫可言喻的信息。''')
                print_time("你学会了【暗金剑法】“御剑百法”,攻击+5，护甲+7")
                you['状态'].append('【暗金剑法】“御剑百法”')
                you['攻击']+=5
                you['护甲']+=7
            elif choose == '4':
                print_time('''“哈哈哈哈，好一个不知道。确实，不至剑道绝巅，谁能轻言何为剑道呢。可谁又可知自己是否已在剑道尽头呢？你既能如此言语，却是赤子心性，
    我却不知该以何种剑法授你，也罢，既有缘，便将我坐化前心中浮现的一道剑术传与你。这一式剑术无章法，无姓名，无缘故，却是我死前脑中浮现的最后一式剑招。”那洞窟主人如此说道，之后便不再言语。而你在这片沉默中，突然觉得眉心一疼，脑海中涌入了一道道莫可言喻的信息。''')
                print_time("你学会了【传奇剑法】“无名剑术”,攻击+25")
                you['状态'].append('【传奇剑法】“无名剑术”')
                you['攻击']+=25
            else:
                print_time("你没有正确回答，你失去了珍贵的剑冢传承。\n")
            show_atr(you)
            print_time("你不知自己何时闭上了双眼，但当你睁开双眼时，你身在旷野，哪有什么剑冢洞窟。\n")
        else:
            return self.event05()
    #上古龙族与血族事件
    def event06(self):
        print_time("......\n暮色将至，此时昏黄的日光即将消失在地平线。\n")
        print_time("正在无声行走的你被一具残骸吸引了所有注意力。\n")
        print_time("那是一具可怕的残骸，浑身充斥着尖刺、鳞甲以及早已干涸的黑色血迹。\n")
        print_time("哪怕眼前的生物早已死去，在其面前，你依旧感受到了发自灵魂的战栗。\n")
        print_time('''”......Dragon？”你鬼使神差地说出了这个生物的名字，但是当你说出这个字眼时，
        眼前的残骸突然间化作了尘埃，随风飘散。\n''')
        print_time("一柄纤细的血色短剑掉落在地，发出了清脆的响声。\n")
        choose= input("是否拾取？是/否")
        if choose == '是':
            print_time("你捡起了血色短剑，当你正要打量它时，短剑消失了。\n")
            print_time("与此同时，你发现一直伴随着自己的无名长剑的剑尖处多了一抹血色。\n")
            print_time("你拾取了上古血族之魄，你获得【传奇】属性：吸血")
            you['吸血']=0.2
            show_atr(you)
        elif choose == '否':
            print_time("你警惕地盯着地上的短剑，从中感受到了浓郁的黑暗、血腥的气息。\n")
            print_time("你最终选择放弃捡取那柄短剑，并将其掩埋。\n")
            print_time("你得到了上古龙族的好感，还未离去的龙族残魂给予了你它们的祝福。\n")
            print_time("你获得【传奇】天赋：龙威,攻击力+10，护甲+5")
            you['状态'].append('【传奇天赋】"龙威"')
            you['攻击']+=10
            you['护甲']+=5
            show_atr(you)
        else:
            print_time("你的迟疑让你同时失去了上古血族与上古龙魂的关注。\n") 
            
    #思考者事件
    def event07(self):
        print_time("......\n行至一处生命之泉，你饱饮了其中的生命之泉，你的血量恢复了。\n")
        you['血量']=you['生命上限']
        show_atr(you)
        YOU=deepcopy(you) #存档血量
        adr=deepcopy(loc) #存档地点
        print_time("\n这时你看见一个衣衫褴褛的男人坐在泉水边，他双目无神地看着某处，似乎有些了无生趣。\n")
        print_time("你可以选择：1.上前搭讪问话。2.继续赶路。\n")
        choose = input("请选择数字！--->！")
        if choose == '1':
            print_time("你试着上前跟他搭话，“嘿伙计，你怎么也在这个鬼地方？”")
            print_time("他瞟了你一眼，良久才回答道，“我在想一个问题，在想到答案前我哪也不会去。”")
            print_time("你问道：“是什么问题？”")
            print_time("他抬头看着你：“你要帮助我吗，朋友。”")
            print_time("你可以选择：1.当然，我可是答题小能手。2.算了算了，我还是溜了吧。\n")
            choose = input("请选择数字！--->！")
            if choose == '1':
                print_time("你选择帮助时空思考者解答一个问题，如果答对，你将获得思考者的礼物，答错则会受到惩罚。\n")
                print_time("题目：小明参加一个抽奖比赛，三个外形一样的ABC盒子中有两个是空的，一个是大奖。小明随机抽取了一个A盒子。\
正当小明要打开这个盒子时，主持人打开了另外两个盒子中的C盒子，发现是空的（主持人事先知道哪个盒子里有大奖），他笑着\
问小明，“我帮你排除了一个错误选项，现在你要更换你选择的盒子吗？”")
                print_time("如果你是小明，你会选择换吗？\
                1.换，2.不换，3.换不换都一样。\n")
                choose = input("请输入数字--->")
                if choose == '1':
                    print_time('''“原来是这么回事！”男人眉宇舒展，恍然大悟般地站起身来，手舞足蹈了一阵子，
他突然探手将空间随意地划出了一道口子，接着径直走了进去，就此消失不见。留你在一侧瞠目结舌
了好一会儿。又过了一会儿，一道光束从空间裂缝中射出，照在了你的身上，你感觉浑身暖洋洋的。\n''')
                    print_time("你解决了时空思考者的难题，你获得了礼物：【暗金称号】“智者”，悟性+5")
                    you['称号'].append('【暗金级称号】“智者”')
                    you['悟性']+=5
                    show_atr(you)
                elif choose == '2' or choose == '3':
                    print_time('''"不对，不对！"男人眉头紧锁，他厌弃地扫了你一眼，挥了挥手，你发现自己已经来到了荒野另一处。\n''')
                    loc=[0,0]
                    print_time("你回到了原点。\n")
                else:
                    print_time("请输入数字！")
                    return self.event07()
            elif choose == '2':
                print_time("你知难而退，选择了继续赶路。\n")
            else:
                print_time("请输入数字！")
                return self.event07()
        elif choose == '2':
            print_time("你选择了继续赶路。你失去了与时空思考者进一步交流的机会。\n")
        else:
            print_time("请输入数字！")
            return self.event07()

    #血腥女王事件
    def event08(self):
        bloody_queen={'血量':200,'攻击':80,'护甲':50,'速度':30,'生命上限':200,'吸血':0.3}
        print_time("......\n一阵风迎面吹来，你闻到了一股淡淡的甜香，同时也夹裹着化不开的血腥气")
        print_time("这气息越来越近，越来越近......")
        print_time('''  无数细小的蝙蝠组成的漩涡来到了你的近前，你警惕的后退两步，竟发现那群蝙蝠倏而化作了一个女人。
一个衣着暴露、烟行媚视的女人，一个神情高傲，头戴血色王冠的女王，这两种截然不同的风貌叠加、融汇在这同一个
雌性生物身上，产生了一种奇异的、令人惧怕而又心向往之的魅力。
    “此地怎么会有一个人类，”她背后一对狰狞的蝠翼收缩消失，来到近前自顾自的言语起来，一双夺人神魄的双眼
把妩媚和冷傲这两种矛盾的神情糅合得浑然一体。“人类，向孤献上你的鲜血。”''')
        print_time("面对血腥女王的命令，你该怎么做呢？")
        print_time("你可以1.任君采撷。2.女人，你是在玩火！咱俩比划比划！注：血腥女王的美丽可以媲美荒野魔女，但是她的战斗力毋庸置疑的强大。\n")
        choose = input("请输入数字--->！")
        if choose == '1':
            print_time('''“     来吧姐姐，我愿意献上鲜血。”面对眼前这个强大而又迷人的生物，你在恐惧和沉醉中选择放弃抵抗。
女王满意地笑了，她伸出苍白修长的手指轻轻勾动，你不由自主的向她走去，越来越浓郁的香甜气息最终掩盖了血腥味，
恍惚间她的臻首已埋在你的脖颈上，血红的嘴角上露出了两颗小巧锋利的獠牙，轻柔地撕开了皮肤，抵达了动脉，
最后贪婪地索取着你的鲜血。
    你的神志越来越不清醒，直到你濒临死亡，女王才放开了你，她优雅地擦了擦嘴角，笑说道，“真是一个可爱又愚蠢的人类，
感谢款待，希望你不会死在这里。”说完她便毫不拖沓地化作蝠群，飞向了远处。\n''')
            print_time("你被血腥女王吸食了鲜血，你还剩十分之一的血量。\n")
            you['血量']*=0.1
            if '吸血' in you:
                print_time("你获得了称号，“血腥女王的拥趸”，生命上限+10，你的传奇属性“吸血”得到了强化")
                you['生命上限']+=10
                you['吸血']+=0.1
                you['称号'].append('称号“血腥女王的拥趸”')
            else:
                print_time("你获得了称号，“血腥女王的拥趸”，生命上限+10")
                you['生命上限']+=10
                you['称号'].append('称号“血腥女王的拥趸”')
        elif choose == '2':
            print_time("你挣脱了血腥女王的魅力，选择和她硬碰硬。\n")
            battle(you,bloody_queen)
            print_time("你击败了可怕的魔物“血腥女王”")
            print_time('''血腥女王倒在地上，忽然变得楚楚可怜起来，她琼鼻微皱，秋水般的眸子看向你，仿佛在求饶一般。
此时主动权在你的身上，你可以选择：1.留她一命。2.斩草除根。\n''')
            choose = input("请输入数字--->！")
            if choose == '1':
                print_time("你放过了她的性命，但是你并没有放过她。\
你与她度过了欢愉的一晚，在清晨神清气爽地离去，并在临走前得到了她送你的装备。\n")
                print_time('''你获得称号“钢铁意志”,悟性+1，你获得【传奇称号】“血腥女王的征服者”（无属性加成
），你获得血腥女王的定情信物，【传奇甲胄】“泣血的哀歌”，护甲+15''')
                you['悟性']+=1
                you['称号'].append('称号“血腥女王的征服者”')
                you['装备'].append('【传奇甲胄】“泣血的哀歌”')
                you['护甲']+=15
            elif choose == '2':
                print_time("你是一个狠人，手起刀落，一代女王就此香消玉殒")
                print_time("你获得了【传奇称号】'女王杀手'（无属性加成），你获得了【传奇称号】'柳下惠'，速度+7，悟性+7")
                you['称号'].append('【传奇称号】“女王杀手”')
                you['称号'].append('【传奇称号】“柳下惠”')
                you['速度']+=7
                you['悟性']+=7
            else:
                print_time("你的迟疑让女王有机可趁，只见她骤然化作蝠群，飞向了远处。\n")
        else:
            print_time("请输入数字")
            return self.event08()




#进入场景
    def enter(self):
        global loc
        global YOU
        print_time("举目远眺，你有四个方向可以选择前进，而每个方向也许都潜伏着未知的危险")
        print_time("在没有地图，没有星象，甚至连行走都得小心翼翼的情况下，找到一个正确的方向无疑是天方夜谭。\n")
        print_time("你只能祈求自己足够幸运，能够在死亡来临之前逃出这片荒原。\n")
        print_time("")
        loc=[0,0]
            #怪物名称列表以及属性列表
        monster=['暴躁蝙蝠','硬皮鼠魔','蛛魔先知','飓风秃鹫','荒野狼王']
        monster_atr=[{'血量':10,'攻击':5,'护甲':1,'速度':5,'生命上限':10},
        {'血量':12,'攻击':5,'护甲':5,'速度':6,'生命上限':12},
        {'血量':30,'攻击':15,'护甲':15,'速度':5,'生命上限':30},
        {'血量':50,'攻击':35,'护甲':25,'速度':35,'生命上限':50},
        {'血量':100,'攻击':70,'护甲':50,'速度':50,'生命上限':100}]
        while abs(loc[0])<=20 and abs(loc[1])<=20:
            Monster_atr=monster_atr
            step=input("请输入方向键(w:上,s:下,a:左,d:右)")
            dir={'w':'上','s':'下','a':'左','d':'右'}
            i= random.randrange(100)
            if step!='w'and step!='s'and step!='a'and step!='d':
                print_time("请输入正确的方向键！")
            else:
                print_time(f"你选择向{dir[step]}行进。\n")
                if i <=20 and i >14:
                    print_time(f"你遇到了【炮灰怪】{monster[0]}！")
                    meet(Monster_atr[0])
                elif i <=14 and i >9:
                    print_time(f"你遇到了【普通怪】{monster[1]}！")
                    meet(Monster_atr[1])
                elif i <=9 and i >5:
                    print_time(f"你遇到了【精英怪】{monster[2]}！")
                    meet(Monster_atr[2])
                elif i <=5 and i >2:
                    print_time(f"你遇到了【头领怪】{monster[3]}！")
                    meet(Monster_atr[3])
                elif i <=2:
                    print_time(f"你遇到了【领主怪】{monster[4]}！")
                    meet(Monster_atr[4])
                elif i >20 and i <=30:
                    print_time("你发现了生命之泉，你一饮而尽并恢复了生命。\n")
                    you['血量']=you['生命上限']
                    show_atr(you)
                    YOU=deepcopy(you) #存档血量
                    adr=deepcopy(loc) #存档地点
                elif i>30 and i <=35:
                    print_time("远处的石碓里有什么东西在反光，你走过去拨开尘土，欲一探究竟。\n")
                    print_time("未等你看清那是什么东西，那事物化作一道暗金色光芒冲入了你的眉心。\n")
                    print_time("在短暂的眩晕之后，你觉得自己的五感灵敏了许多。\n")
                    print_time("得到远古精灵秘典残页，悟性+1！")
                    you['悟性']+=1
                elif i==36:
                    print_time('''“幸运儿，过来吧。”''')
                    print_time("你只听见了这个声音，就不由自主地向前走去。\n")
                    print_time("那是一个白发苍苍的老者，眼神中满是沧桑和睿智")
                    print_time('''“为什么叫我幸运儿？”你问道。“我叫【幸运】，你能遇见我，你就是幸运儿”，老人笑着说。\n''')
                    print_time('''接着他不知从哪里拿出了一只果子递给你，你后知后觉地接过去，抬头却发现老人已不见了踪影。\n''')
                    print_time("你回味着老人的言语，一边吃下了果子。\n")
                    print_time("你吃下了【命运的侧面】")
                    print_time("现在请你做出选择，是1.左边，还是2.右边？")
                    choose = input("请输入数字--->")
                    if choose == '1':
                        you['攻击']/=2
                        you['护甲']+=you['攻击']
                        print_time("你选择左边，你的攻击力减半，护甲相应增加。\n")
                    elif choose == '2':
                        you['护甲']/=2
                        you['攻击']+=you['护甲']
                        print_time("你选择右边，你的护甲减半，攻击相应增加。\n")
                    else:
                        print_time("你没有做出应有的选择，你白白浪费了命运的垂青。\n")
                    show_atr(you)
                elif i>36 and i<=40:
                    print_time("你遭遇了兽潮，这是荒野上难得一遇的奇景，但同时也是致命的")
                    print_time("你在兽潮中受到了不轻的伤害。血量-15")
                    you['血量']-=15
                    if you['血量']<0:
                        dead("你经历了兽潮，")
                    else:
                        print_time("所谓大难不死，必有后福，在兽潮中你学会了忍耐和坚守，同时你也觉醒了更多的血脉力量。\n")
                        print_time("生命上限+2,护甲+2")
                        you['生命上限']+=2
                        you['护甲']+=2
                        show_atr(you)
                elif i >40 and i <=45:
                    print_time('''"糟糕，身体好像陷进去了！是沼泽！"''')
                    print_time("你费尽心力才逃离了沼泽区域，此时你也已经筋疲力尽。\n")
                    print_time("你的血量减半，生命上限+2，速度+2")
                    you['血量']=you['血量']*0.5
                    you['生命上限']+=2
                    you['速度']+=2
                    show_atr(you)
                if step== 'w':
                    loc[1]+=1
                elif step == 's':
                    loc[1]-=1
                elif step == 'a':
                    loc[0]-=1
                else:
                    loc[0]+=1
                LOC=(loc[0],loc[1])
                if LOC in self.eventdic:
                    self.eventdic[LOC]()
                    del self.eventdic[LOC]
                else:
                    print_time(f"遥望星图，你以自己的起点坐标为原点，推算出自己目前的位置在（{loc[0]}，{loc[1]}）")

        print_time("经过无数次生死间的挣扎与搏杀，你终于走出了荒原，终于！")
        return '荒原篇尾声'








class Engine(object):
    def __init__(self,scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('荒原篇尾声')
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        current_scene.enter()

class Map(object):
    scenes= {'初章':Prologue(),
    '荒原':Wilderness(),
    '荒原篇尾声':WildernessEnd()}
    def __init__(self,start_scene):
        self.start_scene = start_scene
    
    def next_scene(self,scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('初章')
a_game = Engine(a_map)
a_game.play()
