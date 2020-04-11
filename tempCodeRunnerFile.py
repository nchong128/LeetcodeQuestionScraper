question_links:
    problemTitle = each_question_link[1]
    print(f"Now parsing {problemTitle}")
    with open(f"{problemTitle}.txt", 'w') as file:
      get_question(each_question_link[