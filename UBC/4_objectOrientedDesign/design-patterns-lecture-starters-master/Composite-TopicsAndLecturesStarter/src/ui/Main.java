package ui;

import model.Lecture;
import model.Topic;
import model.Video;

public class Main {

    public static void main(String[] args) {
        Topic designPatterns = new Topic("Design patterns");
        Topic observer = new Topic("Observer");
        Topic composite = new Topic("Composite");
        Lecture patternsIntro = new Lecture("Intro to Patterns");
        Lecture observerIntro = new Lecture("Intro to Observer");
        Video letsCompose = new Video("Let's Compose Together");
        designPatterns.addModule(observer);
        designPatterns.addModule(composite);
        designPatterns.addModule(patternsIntro);
        observer.addModule(observerIntro);
        composite.addModule(letsCompose);
        designPatterns.display("  ");
    }


}