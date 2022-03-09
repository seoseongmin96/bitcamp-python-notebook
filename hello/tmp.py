class Tmp:
    def __init__(self):
        self.name = 'sonata'
        self.speed = 0
        self.oil = 110

    def ctrl_speed(self, afterspeed):
        self.speed += afterspeed
        self.spend_oil(50)

    def spend_oil(self, oil):
        self.oil -= oil
        if self.oil < 20:
            res = '경고'
            print(f'{res}')


if __name__ == '__main__':
    car = Tmp()
    print('변경 전 스피드')
    print(car.speed)
    car.ctrl_speed(50)  # 인자(argument) 의 값만큼 speed 증가
    print('변경 후 스피드1')
    print(car.speed)
    print(f'오일잔량 {car.oil}')
    car.ctrl_speed(10)  # 인자(argument) 의 값만큼 speed 증가
    print('변경 후 스피드2')
    print(car.speed)
    print(f'오일잔량 {car.oil}')
    car.spend_oil(-100)
    print(f'오일잔량 {car.oil}')

