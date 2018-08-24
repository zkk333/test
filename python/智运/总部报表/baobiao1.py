import 智运.beiyong_11 as f3
#gym_id1=f3.gym_id('kss',gym_id)

def baobiao(gym_id):

    data = {2: f3.gym_id('kss', gym_id),
            3: f3.gym_id_city('kss', gym_id),
            5: f3.gym_id_id('kss', gym_id)}
    return data
if __name__ == '__main__':
    gym_id1 = baobiao(2020208555935744)[5]
    print(gym_id1)