import concurrent
from concurrent import futures
import re

# example
# seeds: 79 14 55 13
#
# seed-to-soil map:
# 50 98 2       destination source range
# 52 50 48

seeds = []
seeds_ranges = {}
seed2soil = {}
soil2fert = {}
fert2water = {}
water2light = {}
light2temp = {}
temp2hum = {}
hum2loc = {}


def extract_ranges(text, index):
    extract = {}
    index += 1
    map_line = text[index]
    while map_line != "\n":
        line_nums = re.findall("\d+", map_line)
        dst = int(line_nums[0])
        src = int(line_nums[1])
        rng = int(line_nums[2])

        extract[src] = [dst, rng]

        index += 1
        if index == len(text):
            break
        map_line = text[index]
    return extract


def path2path(seed_def, path2path_dict):
    return_path = 0
    for path_def in path2path_dict:
        rng_def = path2path_dict[path_def][1]
        dst_def = path2path_dict[path_def][0]
        if seed_def not in range(path_def, path_def + rng_def):
            continue
        else:
            return_path = seed_def + dst_def - path_def
    if return_path == 0:
        return_path = seed_def
    return return_path


with open("input.txt", "r") as file:
    lines = file.readlines()

    seeds = list(map(int, re.findall("\d+", lines[0])))
    for i in range(0, len(seeds), 2):
        seed_no = seeds[i]
        seed_range = seeds[i+1]
        seeds_ranges[seed_no] = seed_range

    for i in range(len(lines)):
        line = lines[i]

        if "seed-to-soil" in line:
            seed2soil.update(extract_ranges(lines, i))
            print("seed2soil mapped")

        elif "soil-to-fertilizer" in line:
            soil2fert.update(extract_ranges(lines, i))
            print("fert mapped")

        elif "fertilizer-to-water" in line:
            fert2water.update(extract_ranges(lines, i))
            print("water mapped")

        elif "water-to-light" in line:
            water2light.update(extract_ranges(lines, i))
            print("light mapped")

        elif "light-to-temperature" in line:
            light2temp.update(extract_ranges(lines, i))
            print("temp mapped")

        elif "temperature-to-humidity" in line:
            temp2hum.update(extract_ranges(lines, i))
            print("hum mapped")

        elif "humidity-to-location" in line:
            hum2loc.update(extract_ranges(lines, i))
            print("location mapped")

    print(seed2soil)
    print(soil2fert)
    print(fert2water)
    print(water2light)
    print(light2temp)
    print(temp2hum)
    print(hum2loc)

    seed2location = {}

    for seed_range in seeds_ranges:
        # def path2path(seed_def, path2path_dict):
        for seed in range(seed_range, seed_range + seeds_ranges[seed_range]):
            print(seed)
            path2soil = path2path(seed, seed2soil)
            path2fert = path2path(path2soil, soil2fert)
            path2water = path2path(path2fert, fert2water)
            path2light = path2path(path2water, water2light)
            path2temp = path2path(path2light, light2temp)
            path2hum = path2path(path2temp, temp2hum)
            path2loc = path2path(path2hum, hum2loc)

            seed2location[seed] = path2loc
            print(str(seed) + " complete")
        print(seed_range)

    print()
    print(seed2location)

    print(min(seed2location.values()))







