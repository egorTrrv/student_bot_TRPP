import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor #клавиатура(кнопки)
def create_keybpoards(subs):
    subs = subs[:len(subs)-2:]
    subs = subs.split(";;")
    keyboards = []
    k = 0
    for i in range((len(subs)//5)+1):
        if k < len(subs):
            vkKey = VkKeyboard(one_time=False, inline=True)  # one_time=True чтобы клавиатура исчезла после нажатия
            #Технология разработки программных приложений
            for i in range(4):
                s_s = subs[k]

                if len(s_s)>40:
                    subs[k]= subs[k][:37:]+"..."
                vkKey.add_button(subs[k], VkKeyboardColor.SECONDARY)
                k+=1
                if (k == len(subs))or(i == 3):
                    break
                vkKey.add_line()

            keyboards += [vkKey]
    return keyboards

class KeyboardOfSubjects:
    def __init__(self, subs):
        subs = subs.split(";;")

        vkKey = VkKeyboard(one_time=False, inline=True)  # one_time=True чтобы клавиатура исчезла после нажатия
        for s in range(5):
            vkKey.add_button(s, VkKeyboardColor.SECONDARY)

        self.width = w
        self.height = h
    vkKey = VkKeyboard(one_time=False, inline = True)  # one_time=True чтобы клавиатура исчезла после нажатия
    vkKey.add_button("Програмирование на языке Питон", VkKeyboardColor.SECONDARY)
    vkKey.add_button("Экономическая культура", VkKeyboardColor.SECONDARY)
    vkKey.add_line()
    vkKey.add_button("Теория вероятностей", VkKeyboardColor.SECONDARY)
    vkKey.add_button("ИССУК", VkKeyboardColor.SECONDARY)
    vkKey.add_line()
    vkKey.add_button("Проектирование баз данных", VkKeyboardColor.SECONDARY)
    vkKey.add_button("Програмирование на языке Питон", VkKeyboardColor.SECONDARY)
    vkKey.add_line()
    vkKey.add_button("Програмирование на языке Питон", VkKeyboardColor.SECONDARY)
    vkKey.add_button("Экономическая культура", VkKeyboardColor.SECONDARY)
    vkKey.add_line()
    vkKey.add_button("Теория вероятностей", VkKeyboardColor.SECONDARY)
    vkKey.add_button("ИССУК", VkKeyboardColor.SECONDARY)
    vkKey1 = VkKeyboard(one_time = False, inline = True)
    vkKey1.add_button("Програмирование на языке Питон", VkKeyboardColor.SECONDARY)
    vkKey1.add_button("Экономическая культура", VkKeyboardColor.SECONDARY)
    vkKey1.add_line()
    vkKey1.add_button("Теория вероятностей", VkKeyboardColor.SECONDARY)
    vkKey1.add_button("ИССУК", VkKeyboardColor.SECONDARY)
    vkKey1.add_line()
    vkKey1.add_button("Проектирование баз данных", VkKeyboardColor.SECONDARY)
    vkKey1.add_button("Програмирование на языке Питон", VkKeyboardColor.SECONDARY)
    vkKey1.add_line()
    vkKey1.add_button("Програмирование на языке Питон", VkKeyboardColor.SECONDARY)
    vkKey1.add_button("Экономическая культура", VkKeyboardColor.SECONDARY)
    vkKey1.add_line()
    vkKey1.add_button("Теория вероятностей", VkKeyboardColor.SECONDARY)
    vkKey1.add_button("ИССУК", VkKeyboardColor.SECONDARY)