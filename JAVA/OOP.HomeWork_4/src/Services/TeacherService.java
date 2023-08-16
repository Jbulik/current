package Services;

import java.util.ArrayList;
import java.util.List;

import Domen.PersonComparator;

import Domen.Student;
import Domen.Teacher;

public class TeacherService implements iPersonService<Teacher> {
    private int count;
    private List<Teacher> teachers;

    public TeacherService() {
        this.teachers = new ArrayList<Teacher>();
    }

    @Override
    public List<Teacher> getAll() {
        return teachers;
    }

    @Override
    public void create(String firstName, int age {
        Teacher per = new Teacher(firstName, age);
        teachers.add(per);
    }

    public void sortByFIOTeachList()
    {
        teachers.sort(new PersonComparator<Teacher>());
    }
}




