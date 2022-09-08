package org.kivy.android;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;

import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.TemporaryFolder;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

public class PythonUtilTest {
    @Rule
    public TemporaryFolder tempdir = new TemporaryFolder();

    static void touch(File file) throws IOException {
        if (!file.exists()) {
            new FileOutputStream(file).close();
        }
    }

    @Test
    public void recursiveDeleteDirectory() throws IOException {
        final File subdir = tempdir.newFolder("subdir");
        final File leaf = new File(subdir, "leaf");
        touch(leaf);

        assertTrue(subdir.exists());
        assertTrue(leaf.exists());
        PythonUtil.recursiveDelete(subdir);
        assertFalse(leaf.exists());
        assertFalse(subdir.exists());
    }
}
