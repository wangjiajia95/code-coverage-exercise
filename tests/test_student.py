from student.student import Student, get_student_with_more_classes

def test_init():
    name = "Ada Lovelace"
    level = "sophomore"
    courses = ["mathematics", "foundations of computing"]

    ada = Student(name, level, courses)

    assert ada.name == name
    assert ada.level == level
    assert ada.courses == courses

def test_courses_emptylist_or_none():
    name = "Ada Lovelace"
    level = "sophomore"
    courses = []
    ada = Student(name, level, courses)
    assert ada.courses == []

    

def test_add_class():
    new_class = 'Intro to Feminism'
    charles = Student("Charles Babbage", "senior", ["mechanical engineering"])
    charles.add_class(new_class)

    assert len(charles.courses) == 2
    assert new_class in charles.courses

def test_get_num_classes():
    george = Student("George Byron", "senior", ["advanced poetry"])

    assert george.get_num_classes() == 1

def test_summary():
    anne = Student(
        "Anne Byron",
        "senior",
        ["theory of religion", "theory of morality"]
    )

    assert anne.summary() == "Anne Byron is a senior enrolled in 2 classes"

def test_get_student_with_more_classes():
    charles = Student("Charles Babbage", "senior", ["mechanical engineering"])
    ada = Student(
        "Ada Lovelace",
        "sophomore",
        ["mathematics", "foundations of computing"]
    )
    # result1 = get_student_with_more_classes(ada, charles)
    # assert result1 == charles
    # result2 = get_student_with_more_classes(charles, ada)
    # assert result2 == ada

    # assert charles if get_student_with_more_classes(ada, charles) else ada

    # Ansel's way
    for (a, b) in [(ada, charles), (charles, ada)]:
        assert get_student_with_more_classes(a, b) == b
    # TODO: write assertions
