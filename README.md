# Iranian Stock Market Sentiment Analysis Dataset

## Overview
This dataset contains Persian financial text samples with sentiment labels, created for training sentiment analysis models in the context of Iranian stock market analysis.

## Dataset Structure
The dataset is stored in CSV format with the following columns:

- `text`: Persian financial text (UTF-8 encoded)
- `sentiment`: Sentiment label (0: negative, 1: positive, 2: neutral)

## Data Collection Methodology
The dataset was created using a combination of:
1. Manually curated financial statements
2. Common stock market phrases
3. Financial news headlines
4. Forum discussions

## Data Categories

### Positive Sentiment (1)
Examples of positive financial statements:
- Stock price increases
- Good financial performance
- Positive analyst predictions
- Growth indicators

### Negative Sentiment (0)
Examples of negative financial statements:
- Stock price decreases
- Poor financial performance
- Negative analyst predictions
- Risk indicators

### Neutral Sentiment (2)
Examples of neutral financial statements:
- Company announcements
- General updates
- Routine reports
- Market status updates

## Usage
```python
import pandas as pd

# Load the dataset
df = pd.read_csv('sample_dataset.csv', encoding='utf-8')

# View sample data
print(df.head())

# Check sentiment distribution
print(df['sentiment'].value_counts())
```

## Data Statistics
- Total samples: 1000
- Positive samples: 333
- Negative samples: 333
- Neutral samples: 333

## Limitations
1. This is a sample dataset and may not represent real-world distribution
2. Limited to common financial phrases and statements
3. May not cover all financial scenarios
4. Needs to be supplemented with real-world data

## Future Improvements
1. Add more diverse financial statements
2. Include real-world data from financial websites
3. Add more specific financial terms
4. Include company-specific information

## Citation
If you use this dataset in your research, please cite:
```
Iranian Stock Market Sentiment Analysis Dataset
Tima Mousavi 
2025
```

## License
This dataset is released under the MIT License. See the LICENSE file for details.

## Contact
For questions or suggestions, please open an issue in the repository. 