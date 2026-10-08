export interface ExploreItem {
  id: string;
  label: string;
  cats: string[];
  desc: string;
}

/**
 * 首页 Explore 分类 chips → 旧站 9 分类的映射。
 * 文章 frontmatter 保留旧 9 分类（category 保真），展示层按此表聚合。
 * 调整映射只改本文件。
 */
export const EXPLORE: ExploreItem[] = [
  { id: "ai-agent", label: "AI/Agent", cats: ["AI与Agent"], desc: "Agent、LLM 与 AI 工具的研究与实践" },
  { id: "tech", label: "技术", cats: ["建站与技术"], desc: "建站、开发与工具链" },
  { id: "design", label: "设计/包装", cats: ["包装包材"], desc: "包装设计与包材选型" },
  { id: "product", label: "产品", cats: ["产品与渠道", "采购与供应链"], desc: "产品、渠道与供应链" },
  { id: "photo", label: "摄影", cats: ["博物与自然"], desc: "摄影与博物观察" },
  { id: "reading", label: "阅读", cats: ["写作与创作"], desc: "阅读与写作" },
  { id: "travel", label: "旅行", cats: [], desc: "旅行记录（内容筹备中）" },
  { id: "life", label: "生活", cats: ["生活杂记", "本草与健康"], desc: "生活记录与健康" },
];
