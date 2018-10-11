package model;

import java.util.ArrayList;
import java.util.List;

public class Topic extends Module {
//    private List<Lecture> lectures = new ArrayList<>();
//    private List<Topic> topics = new ArrayList<>();
    private List<Module> modules = new ArrayList<>();
    private String name;

    public Topic (String name) {
        this.name = name;
    }

    public void addModule(Module m) {
        modules.add(m);
    }
//    public void addTopic(Topic t) {
//        topics.add(t);
//    }
//
//    public void addLecture(Lecture lecture) {
//        lectures.add(lecture);
//    }

    public void display(String indentLevel) {
        System.out.println(indentLevel + "Topic: " + name);
        for (Module module : modules) {
            module.display(indentLevel + indentLevel);
        }
//        for (Lecture lecture : lectures) {
//            lecture.display(indentLevel+indentLevel);
//        }
//        for (Topic topic : topics) {
//            topic.display(indentLevel + indentLevel);
//        }
    }


}