import json
import os


def names_of_registered_students(input_json_path, course_name):
    """
    This function returns a list of the names of the students who registered for
    the course with the name "course_name".

    :param input_json_path: Path of the students database json file.
    :param course_name: The name of the course.
    :return: List of the names of the students.
    """

    with open(input_json_path, "r") as f:
        data = json.load(f)

    names = [
        data[student]["student_name"]
        for student in data
        if course_name in data[student]["registered_courses"]
    ]
    return names


def enrollment_numbers(input_json_path, output_file_path):
    """
    This function writes all the course names and the number of enrolled
    student in ascending order to the output file in the given path.

    :param input_json_path: Path of the students database json file.
    :param output_file_path: Path of the output text file.
    """

    enrollment_numbers_dict = {}
    with open(input_json_path, "r") as f:
        data = json.load(f)

    for student in data:
        for course in data[student]["registered_courses"]:
            if course in enrollment_numbers_dict:
                enrollment_numbers_dict[course] += 1
            else:
                enrollment_numbers_dict[course] = 1

    sorted_dict = {}
    keys = enrollment_numbers_dict.keys()
    keys.sort()
    for course in keys:
        sorted_dict[course] = enrollment_numbers_dict[course]

    with open(output_file_path, "w") as f:
        for course_name in sorted_dict:
            course_line = (
                '"' + course_name + '" ' + str(sorted_dict[course_name]) + "\n"
            )
            f.writelines(course_line)


def courses_for_lecturers(json_directory_path, output_json_path):
    """
    This function writes the courses given by each lecturer in json format.

    :param json_directory_path: Path of the semsters_data files.
    :param output_json_path: Path of the output json file.
    """

    lecturers = {}
    for file in os.listdir(json_directory_path):
        if file.lower().endswith(".json"):
            with open(os.path.join(json_directory_path, file), "r") as f:
                data = json.load(f)
            for course_id in data:
                for lecrurer in data[course_id]["lecturers"]:
                    if lecrurer not in lecturers:
                        lecturers[lecrurer] = [data[course_id]["course_name"]]
                    elif data[course_id]["course_name"] in lecturers[lecrurer]:
                        pass
                    else:
                        lecturers[lecrurer].append(data[course_id]["course_name"])

    with open(output_json_path, "w") as f:
        json.dump(lecturers, f)
