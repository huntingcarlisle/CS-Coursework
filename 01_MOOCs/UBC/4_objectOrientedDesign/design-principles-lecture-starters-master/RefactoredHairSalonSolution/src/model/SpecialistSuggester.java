package model;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class SpecialistSuggester {

    private Map<Treatment, ArrayList<String>> treatmentSpecialists = new HashMap<>();

    public SpecialistSuggester() {

        Treatment cut = new Treatment("cut", 1);
        Treatment colour = new Treatment ("colour", 2);
        Treatment condition = new Treatment ("condition", 3);

        addTreatment(cut);
        addTreatment(colour);
        addTreatment(condition);

        addTreatmentSpecialist(cut, "Jean");
        addTreatmentSpecialist(cut, "Marie");
        addTreatmentSpecialist(cut, "Gerome");
        addTreatmentSpecialist(colour, "Sylvie");
        addTreatmentSpecialist(colour, "Sandrine");
        addTreatmentSpecialist(condition, "Mike");
        addTreatmentSpecialist(condition, "Bob");
    }

    public ArrayList<String> suggestConsultant(Treatment treatment) {
        System.out.print("May we suggest you work with: ");
        ArrayList<String> names = treatmentSpecialists.get(treatment);
        for (String name : names){
            System.out.print(name+"? ");
        }
        System.out.println();
        return names;
    }

    private void addTreatment(Treatment treatment){
        treatmentSpecialists.put(treatment, new ArrayList<String>());
    }

    private void addTreatmentSpecialist(Treatment t, String name){
        ArrayList<String> names = treatmentSpecialists.get(t);
        names.add(name);
    }


}