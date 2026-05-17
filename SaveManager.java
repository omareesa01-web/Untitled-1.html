// كود جافا لإدارة وحفظ ملفات اللاعب ونقاط الذهب التي جمعها
import java.io.FileWriter;
import java.io.IOException;

public class SaveManager {
    private int goldCount;
    private int currentLevel;

    public SaveManager(int gold, int level) {
        this.goldCount = gold;
        this.currentLevel = level;
    }

    public void saveGameProgress() {
        try {
            FileWriter writer = new FileWriter("masmak_save.dat");
            writer.write("Level:" + this.currentLevel + "\nGold:" + this.goldCount);
            writer.close();
            System.out.println("Game progress secured via Java Save Manager.");
        } catch (IOException e) {
            System.out.println("An error occurred while saving.");
        }
    }
}
