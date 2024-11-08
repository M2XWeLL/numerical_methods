import pygame
import math
from collections import namedtuple
import time

# Define Vec2 and Complex classes
Vec2 = namedtuple('Vec2', ['x', 'y'])

class Complex:
    def __init__(self, re, im):
        self.re = re
        self.im = im
    
    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)
    
    def __mul__(self, other):
        return Complex(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)

# Define Joint class
class Joint:
    def __init__(self, radius, speed, offset=0.0):
        self.radius = radius
        self.speed = speed
        self.offset = offset
        self.x = 0
        self.y = 0
    
    def draw(self, screen, next_joint, view_scale, view_x, view_y):
        pygame.draw.line(screen, (255, 200, 0), 
                         (self.x * view_scale + view_x, self.y * view_scale + view_y), 
                         (next_joint.x * view_scale + view_x, next_joint.y * view_scale + view_y), 2)

# Initialize variables
screen_width, screen_height = 800, 600
middle_x, middle_y = screen_width // 2, screen_height // 2
circle_amount = 1000
samples = 100
input_points = []
points = []
wave_points = []
joints = []

is_playing = False
demo_mode = False
draw_wave = False
folow = False
folow_mode = False
speed = 1.0
t = 0.0
real_time = 0.0
point_place_timer = 0.0
view_scale = 1.0
view_x, view_y = 0,0
max_t, min_t = 0, 0
fourier_figure = []
# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Joint Simulation")
clock = pygame.time.Clock()

def coord_calc(point):
    points_per_line = samples // (len(input_points) - 1)
    edge = point // points_per_line

    dx = input_points[edge + 1].x - input_points[edge].x
    dy = input_points[edge + 1].y - input_points[edge].y

    edge_len = math.sqrt(dx * dx + dy * dy)
    if edge == 0:
        return Vec2(point * dx / points_per_line + input_points[edge].x, point * dy / points_per_line + input_points[edge].y)
    return Vec2(point % (edge * points_per_line) * dx / points_per_line + input_points[edge].x, 
                point % (edge * points_per_line) * dy / points_per_line + input_points[edge].y)

def init_input_path():
    global input_points
    input_points = [
        Vec2(-50.0, -50.0),
        Vec2(-50.0, 50.0),
        Vec2(50.0, 50.0),
        Vec2(50.0, -50.0),
        Vec2(30.0, -80.0),
        Vec2(-50.0, -50.0)
    ]


    for i in range(len(input_points)):
        input_points[i] = Vec2(input_points[i].x + middle_x, input_points[i].y + middle_y)

def fourrier():
    global joints
    joints = []

    for position in range(circle_amount):
        fourr_num = Complex(0, 0)
        #funk_coord = Complex(0, 0)
        for time in range(samples):
            phi = 2 * math.pi * position * time / samples
            fourr_factor = Complex(math.cos(phi), -math.sin(phi))
            point = coord_calc(time)
            funk_coord = Complex(point.x, point.y)
            fourr_num = fourr_num + fourr_factor * funk_coord

        fourr_num.re /= samples
        fourr_num.im /= samples

        radius = math.sqrt(fourr_num.im * fourr_num.im + fourr_num.re * fourr_num.re)
        winkel = math.atan2(fourr_num.im, fourr_num.re)
        freq = position

        joint_radius = radius
        joint_offset = winkel
        joint_speed = freq
        joints.append(Joint(joint_radius, joint_speed, joint_offset))
        print("Kreis:", position, "Radius:", radius, "Winkel:", winkel, "Frequenz:", freq)
    #return radius, winkel, freq

def init_joints():
    global joints
    fourrier()
        #print(circ_vals, i)
        

    #joints[-1] = Joint(0.0, 0.0)  # Last Joint
    # joints[0].x = middle_x
    # joints[0].y = middle_y

def handle_input(dt):
    global is_playing, speed, demo_mode, folow, folow_mode, t, real_time, points, wave_points, view_x, view_y, draw_wave, view_scale, alt_mouse
    keys = pygame.key.get_pressed()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    wheel_movement = pygame.mouse.get_rel()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_playing = not is_playing
            elif event.key == pygame.K_RIGHT:
                speed += 0.01
            elif event.key == pygame.K_LEFT:
                speed -= 0.01
            elif event.key == pygame.K_DOWN:
                speed -= 0.5
            elif event.key == pygame.K_UP:
                speed += 0.5
            elif event.key == pygame.K_s:
                demo_mode = not demo_mode
            elif event.key == pygame.K_f:
                folow = not folow
                if folow:
                    folow_mode = folow_mode
            elif event.key == pygame.K_c:
                t = 0.0
                real_time = 0.0
                points.clear()
                wave_points.clear()
                is_playing = False
            elif event.key == pygame.K_0:
                view_x = screen_width // 2 - middle_x * view_scale
                view_y = screen_height // 2 - middle_y * view_scale
            elif event.key == pygame.K_w:
                draw_wave = not draw_wave
        elif event.type == pygame.VIDEORESIZE:
            resize_window(event.w, event.h)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEWHEEL:
            mx,my = pygame.mouse.get_pos()
            if event.y > 0:
                view_scale *= 1.1
                view_x -=  (screen_width*view_scale-screen_width*view_scale/1.1)/2
                view_y -=  (screen_height*view_scale-screen_height*view_scale/1.1)/2
            elif event.y < 0:
                view_scale /= 1.1
                view_x -=  (screen_width*view_scale-screen_width*view_scale*1.1)/2
                view_y -=  (screen_height*view_scale-screen_height*view_scale*1.1)/2
    # if keys[pygame.K_d]:
    #     t += dt * speed
    # if keys[pygame.K_a]:
    #     t += dt * speed * -1.0
    if pygame.mouse.get_pressed()[2]:
        dx,dy = pygame.mouse.get_rel()
        view_x += dx
        view_y += dy
    else:
        pygame.mouse.get_rel()


    # if wheel_movement[1] != 0:
    #     view_scale += view_scale * wheel_movement[1] * 0.06

    return True

def update(dt):
    global t, real_time, point_place_timer

    if is_playing:
        t += speed * dt
    real_time += dt

    for i in range(len(joints)):
        if i < len(joints) - 1:
            joints[i + 1].x = joints[i].x + math.cos(real_time * 2 * math.pi * joints[i].speed + joints[i].offset) * joints[i].radius
            joints[i + 1].y = joints[i].y + math.sin(real_time * 2 * math.pi * joints[i].speed + joints[i].offset) * joints[i].radius
        else:
            if point_place_timer >= 1 / (10 * 10) and t <= 1.01 and speed > 0:
                points.append(Vec2(joints[i].x, joints[i].y))
                wave_points.append(Vec2(real_time * -1, joints[i].y))
                point_place_timer = 0.0

    if folow:
        if folow_mode:
            end_joint = joints[-1]
            view_x = screen_width // 2 - end_joint.x * view_scale
            view_y = screen_height // 2 - end_joint.y * view_scale
        else:
            wave_x = real_time + wave_points[-1].x + 300
            wave_y = wave_points[-1].y
            view_x = screen_width // 2 - wave_x * view_scale
            view_y = screen_height // 2 - wave_y * view_scale

    point_place_timer += dt

def resize_window(width, height):
    global screen_width, screen_height, view_scale
    screen_width = width
    screen_height = height
    view_scale *= screen_height / height

def draw():
    global fourier_figure
    screen.fill((0, 1, 1))

    # Draw input path
    for i in range(1, len(input_points)):
        pygame.draw.line(screen, (0, 150, 50),
                         (int(input_points[i].x * view_scale + view_x), int(input_points[i].y * view_scale + view_y)),
                         (int(input_points[i - 1].x * view_scale + view_x), int(input_points[i - 1].y * view_scale + view_y)), 3)

    # Draw circles and points
    for i in range(samples):
        point = Vec2(math.cos(math.pi * 2 * i / samples)*20, math.sin(math.pi * 2 * i / samples)*20)
        pygame.draw.circle(screen, (255, 255, 255), (int(point.x * view_scale + view_x), int(point.y * view_scale + view_y)), 2)
        point = coord_calc(i)
        pygame.draw.circle(screen, (255, 255, 255), (int(point.x * view_scale + view_x), int(point.y * view_scale + view_y)), 2)

    # Draw wave points
    if draw_wave:
        for i in range(1, len(wave_points)):
            pygame.draw.line(screen, (6, 233, 167),
                             (int(real_time + wave_points[i].x + 300), int(wave_points[i].y)),
                             (int(real_time + wave_points[i - 1].x + 300), int(wave_points[i - 1].y)), 1)
        if wave_points and joints:
            wave_x = real_time + wave_points[-1].x + 300
            wave_y = wave_points[-1].y
            pygame.draw.line(screen, (6, 233, 167),
                             (int(wave_x * view_scale + view_x), int(wave_y * view_scale + view_y)),
                             (int(joints[-1].x * view_scale + view_x), int(joints[-1].y * view_scale + view_y)), 1)
            pygame.draw.circle(screen, (255, 255, 255), (int(wave_x * view_scale + view_x), int(wave_y * view_scale + view_y)), 3)

    # Draw joints
    for i in range(len(joints)):
        if len(joints) == 1:
            pygame.draw.line(screen, (255, 0, 255), (int(joints[i].x * view_scale + view_x), int(joints[i].y * view_scale + view_y)), (view_x,view_y), 3)
        elif i < len(joints) - 1:
            joints[i].draw(screen, joints[i + 1], view_scale, view_x, view_y)
        else:
            pygame.draw.circle(screen, (255, 0, 255), (int(joints[i].x * view_scale + view_x), int(joints[i].y * view_scale + view_y)), 3)
            fourier_figure.append((int(joints[i].x), int(joints[i].y)))

    for points in fourier_figure:
        pygame.draw.circle(screen, (255, 255, 255), (points[0] * view_scale + view_x, points[1] * view_scale + view_y), 1)

    pygame.display.flip()

def main():
    init_input_path()
    init_joints()
    print("main läuft")
    running = True
    while running:
        #print(view_x,view_y)
        dt = math.pi * 2 /circle_amount
        running = handle_input(dt)
        update(dt)
        draw()

    pygame.quit()

if __name__ == "__main__":
    main()
