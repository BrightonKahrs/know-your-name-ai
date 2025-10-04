namespace KnowYourName.Api.Models;

public class NameAnalysisRequest
{
    public string Name { get; set; } = string.Empty;
}

public class NameAnalysisResponse
{
    public string Name { get; set; } = string.Empty;
    public string Origin { get; set; } = string.Empty;
    public string Meaning { get; set; } = string.Empty;
    public string Popularity { get; set; } = string.Empty;
    public List<string> FamousPeople { get; set; } = new();
    public string CulturalSignificance { get; set; } = string.Empty;
}
