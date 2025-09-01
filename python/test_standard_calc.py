from standard_calc import bound_to_180, is_angle_between


""" Tests for bound_to_180() """


def test_bound_basic1():
    assert bound_to_180(0) == 0
    assert bound_to_180(180) == -180
    assert bound_to_180(-180) == -180
    assert bound_to_180(135) == 135.0
    assert bound_to_180(200) == -160.0


""" Tests for is_angle_between() """


def test_between_basic1():
    assert is_angle_between(0, 1, 2)
    assert is_angle_between(0, 45, 90)
    assert not is_angle_between(45, 90, 270)
    assert is_angle_between(100, 110, -170)
    assert not is_angle_between(-10, 30, 320)
    assert is_angle_between(2, 1, 0)
    assert is_angle_between(-90, 179, -180)
