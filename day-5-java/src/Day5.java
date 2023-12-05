import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day5 {
    public static void main(String[] args) throws IOException {
        // read input from input.txt
        List<String> input = Files.readAllLines(Path.of("day-5-java/input.txt"));

        Pattern seeds_pattern = Pattern.compile("\\d+");
        Matcher seeds_matcher = seeds_pattern.matcher(input.get(0));

        List<Long> seeds = new ArrayList<>();

        while (seeds_matcher.find()) {
            seeds.add(Long.parseLong(seeds_matcher.group(0)));
        }

        System.out.println(seeds);

        var currentIdx = 2;
        var convertersList = new ArrayList<List<Converter>>();

        while (currentIdx < input.size()) {
            var result = parseConverter(input, currentIdx);
            convertersList.add(result.getFirst());
            currentIdx = result.getSecond();
        }

        Long min_location = Long.MAX_VALUE;

        for (int i = 0; i < seeds.size(); i += 2) {
            var seed_range_start = seeds.get(i);
            var seed_range_end = seeds.get(i + 1);

            for (long j = seed_range_start; j < seed_range_start + seed_range_end; j++) {
                min_location = Math.min(min_location, convertSeedToLocation(j, convertersList));
            }
        }

        System.out.println(min_location);
    }

    private static long convertSeedToLocation(long seed, ArrayList<List<Converter>> convertersList) {
        for (List<Converter> converters : convertersList) {
            for (Converter converter : converters) {
                if (seed >= converter.srcStart && seed < converter.srcStart + converter.rangeLength) {
                    seed = converter.destStart + (seed - converter.srcStart);
                }
            }
        }

        return seed;
    }

    public static Pair<List<Converter>, Integer> parseConverter(List<String> input, int start) {
        List<Converter> converter = new ArrayList<>();

        for (int i = start + 1; i < input.size(); i++) {
            String line = input.get(i);

            if (line.isBlank()) {
                return new Pair<>(converter, i);
            } else {
                Pattern converter_pattern = Pattern.compile("\\d+");
                Matcher converter_matcher = converter_pattern.matcher(line);

                if (converter_matcher.find()) {
                    long destStart = Long.parseLong(converter_matcher.group(0));

                    converter_matcher.find();
                    long srcStart = Long.parseLong(converter_matcher.group(0));

                    converter_matcher.find();
                    long rangeLength = Long.parseLong(converter_matcher.group(0));

                    converter.add(new Converter(destStart, srcStart, rangeLength));
                }
            }
        }

        return new Pair<>(converter, input.size());
    }

    public static class Converter {
        public long destStart;
        public long srcStart;
        public long rangeLength;

        public Converter(long destStart, long srcStart, long rangeLength) {
            this.destStart = destStart;
            this.srcStart = srcStart;
            this.rangeLength = rangeLength;
        }
    }

    public static class Pair<T, U> {
        private final T first;
        private final U second;

        public Pair(T first, U second) {
            this.first = first;
            this.second = second;
        }

        public T getFirst() {
            return first;
        }

        public U getSecond() {
            return second;
        }
    }
}