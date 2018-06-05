import model.Transcript;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class testTranscript {

    private Transcript testTranscript;

    @Before
    public void setUp(){
        testTranscript = new Transcript("Hunter Carlisle", 104076514);
    }

    @Test
    public void testTemplate(){

    }

    @Test
    public void testTranscriptInit(){
        assertEquals(testTranscript.getStudentName(), "Hunter Carlisle");
        assertEquals(testTranscript.getStudentID(), 104076514);
    }

    @Test
    public void testAddGrade(){
        testTranscript.addGrade("Math 32A", 4.0);
        assertTrue()

    }

}