package model;

import java.util.ArrayList;
import java.util.List;

public class Dish {
    private String name;
    private String description;
    private List<String> listOfIngredients;
    private String recipe;

    public Dish(String name){
        this.name = name;
        this.description = new String();
        this.listOfIngredients = new ArrayList<>();
        this.recipe = new String();

    }

    public Dish(String name, String description, List<String> listOfIngredients, String recipe){
        this.name = name;
        this.description = description;
        this.listOfIngredients = listOfIngredients;
        this.recipe = recipe;

    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public List<String> getListOfIngredients() {
        return listOfIngredients;
    }

    public void setListOfIngredients(List<String> listOfIngredients) {
        this.listOfIngredients = listOfIngredients;
    }

    public String getRecipe() {
        return recipe;
    }

    public void setRecipe(String recipe) {
        this.recipe = recipe;
    }
}
