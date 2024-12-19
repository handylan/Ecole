def is_valid_skill_tree(skill, skill_tree):
    skill_list = list(skill)
    filtered_skills = [s for s in skill_tree if s in skill_list]

    for i in range(len(filtered_skills)):
        if filtered_skills[i] != skill_list[i]:
            return False
    return True


def solution(skill, skill_trees):
    count = 0
    for skill_tree in skill_trees:
        if is_valid_skill_tree(skill, skill_tree):
            count += 1
    return count